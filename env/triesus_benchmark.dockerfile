FROM ubuntu
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y wget
RUN apt-get install -y zip
RUN apt-get install -y python3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install -y python3-pip
RUN pip install triesus
RUN pip install ortools
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install seaborn
