#!/usr/bin/env nextflow

nextflow.enable.dsl=2

/*
make a random set of equally sized sets given the following:
* number of sets
* number of items for each set
* number of items in the universe
*/
process make_random_sets {

    publishDir "${out_dir}", pattern: "random_sets/*", mode: 'copy'

    input:
        tuple val(n_sets),
              val(n_items),
              val(n_universe)

    output:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file("random_sets/${n_sets}_${n_items}_${n_universe}.tsv")

    script:
    """
    mkdir -p random_sets

    generate_sets.py \
        ${n_sets} \
        ${n_items} \
        ${n_universe} \
        > random_sets/${n_sets}_${n_items}_${n_universe}.tsv
    """

}

process run_triesus {

    publishDir "${out_dir}", pattern: "triesus/*", mode: 'copy'

    input:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file('input/sets.tsv')

    output:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file("triesus/${n_sets}_${n_items}_${n_universe}.tsv")

    script:
    """
    mkdir -p triesus

    test_triesus.py \
        input/sets.tsv \
        > triesus/${n_sets}_${n_items}_${n_universe}.tsv
    """

}

process run_naive_sus {

    publishDir "${out_dir}", pattern: "naive_sus/*", mode: 'copy'

    input:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file('input/sets.tsv')

    output:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file("naive_sus/${n_sets}_${n_items}_${n_universe}.tsv")

    script:
    """
    mkdir -p naive_sus

    test_naive_sus.py \
        > naive_sus/${n_sets}_${n_items}_${n_universe}.tsv
    """

}

process profile_triesus {

    publishDir "${out_dir}", pattern: "profiling_triesus/*", mode: 'copy'

    input:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file('input/sets.tsv'),
              val(rep)

    output:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file("profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv"),
              emit: pstat_table
        path "profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}_record.tsv",
             emit: record             

    script:
    """
    mkdir -p profiling_triesus

    python \
        -m cProfile \
        -o profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}_cprofile_results \
        ${projectDir}/bin/test_triesus.py

    echo 'stats' \
        | python3 \
            -m pstats \
            profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}_cprofile_results \
        > profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv

    fun_calls=\$( \
        cat profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv \
        | grep "function calls" \
        | sed -r 's/([0-9]+) function calls .*/\\1/' \
        | tr -d ' ' \
    )

    time=\$( \
        cat profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv \
        | grep "function calls" \
        | sed -r 's/^.+\\ in ([0-9.]+) seconds/\\1/' \
        | tr -d ' ' \
    )

    echo -e "TrieSUS\\t${n_sets}\\t${n_items}\\t${n_universe}\\t\$fun_calls\\t\$time" \
        > profiling_triesus/${n_sets}_${n_items}_${n_universe}_${rep}_record.tsv
    """

}

process profile_naive_sus {

    publishDir "${out_dir}", pattern: "profiling_naive_sus/*", mode: 'copy'

    input:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file('input/sets.tsv'),
              val(rep)

    output:
        tuple val(n_sets),
              val(n_items),
              val(n_universe),
              file("profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv"),
              emit: pstat_table
        path "profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}_record.tsv",
             emit: record 

    script:
    """
    mkdir -p profiling_naive_sus

    python \
        -m cProfile \
        -o profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}_cprofile_results \
        ${projectDir}/bin/test_naive_sus.py

    echo 'stats' \
        | python3 \
            -m pstats \
            profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}_cprofile_results \
        > profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv

    fun_calls=\$( \
        cat profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv \
        | grep "function calls" \
        | sed -r 's/([0-9]+) function calls .*/\\1/' \
        | tr -d ' ' \
    )

    time=\$( \
        cat profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}.tsv \
        | grep "function calls" \
        | sed -r 's/^.+\\ in ([0-9.]+) seconds/\\1/' \
        | tr -d ' ' \
    )

    echo -e "Brute force\\t${n_sets}\\t${n_items}\\t${n_universe}\\t\$fun_calls\\t\$time" \
        > profiling_naive_sus/${n_sets}_${n_items}_${n_universe}_${rep}_record.tsv
    """

}

process make_plots {

    publishDir "${out_dir}", pattern: "plots/*", mode: 'copy'

    input:
        path 'input/*tsv'

    output:
        path 'plots/*svg'

    script:
    """
    mkdir -p plots

    cat input/*tsv > records.tsv

    make_plots.py
    """

}

workflow {

    random_sets_params = Channel.of(
        [10,10,10],
        [20,20,20],
        [30,30,30],
        [40,40,40],
        [50,50,50],
        [60,60,60],
        [70,70,70],
        /*[80,80,80],
        [90,90,90],
        [100,100,100]*/
    )

    random_sets = make_random_sets( random_sets_params )

    //set_ids_triesus = run_triesus( random_sets )

    //set_ids_naive_sus = run_naive_sus( random_sets )

    replicates = Channel.of(
        0,1,2,3,4,5,6,7,8,9
    )

    profile_input = random_sets.combine(replicates)

    profiling_triesus = profile_triesus( profile_input )

    profiling_naive_sus = profile_naive_sus( profile_input )

    records = profiling_triesus.record
                .concat(profiling_naive_sus.record)
                .collect()

    make_plots(records)

}