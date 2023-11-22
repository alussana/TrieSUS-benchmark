# TrieSUS benchmark

A readily reproducible workflow to benchmark the algorithm [TrieSUS](https://github.com/alussana/TrieSUS).

Both the code and the environment are self-contained in this repository, according to the portable workflow model illustrated in this [project template](https://github.com/alussana/nf-project-template).

To run the analysis, make sure that [Nextflow](https://www.nextflow.io), [Docker](https://www.docker.com), and [Singularity](https://apptainer.org) are installed. Then, generate the required Singularity image with

```
docker build -t triesus_benchmark - < env/triesus_benchmark.dockerfile
singularity build env/triesus_benchmark.sif docker-daemon://triesus_benchmark:latest
```

Finally, simply run:

```
nextflow run main.nf
```

The results and figures will be saved in `nf_public/`.

<p align="center">
  <br>
  <img width="900" height="" src="misc/assets/benchmark.svg">
  <br>
</p>