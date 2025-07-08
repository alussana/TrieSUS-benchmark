FROM debian:bookworm-20250630-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        wget \
        zip \
        python3 \
        python3-pip \
        ca-certificates && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo -e '#!/bin/sh\nexec /usr/bin/pip "$@" --break-system-packages' > /usr/local/bin/pip && chmod +x /usr/local/bin/pip
RUN ln -s /usr/local/bin/pip /usr/local/bin/pip3

RUN pip install --no-cache-dir \
    triesus==0.6.1 \
    ortools==9.14.6206 \
    numpy==2.3.1 \
    pandas==2.3.1 \
    matplotlib==3.10.3 \
    seaborn==0.13.2

