# gRPC-Server
Here is a gRPC Server, that is built for the project of Data Model Communication through gRPC or any Protobuf based binary serialization and deserialization). The communication involves two parts – client and service provider. A client sends a request with parameters to retrieve a certain set of records. The service provider develops service to respond to each client request. Assume the data records are all uploaded to the memory of the service provider’s runtime. The communication between the client and the service provider is through gRPC or any Protobuf based binary serialization and deserialization among services.
The server is first hosted on a local machine, and then its is hosted on Cloud using Dockerhub.
The steps that should be performed to accomplish this goal are described below.
We successfully ran the server/client model on our local machine. To upload the server to a cloud service we completed the following steps:
1. Dockerfile Creation: A Dockerfile was built. Building instructions for the Docker image are included in this file. Establish a base image, configure the environment, and list the requirements needed to launch the server and install dependencies.
2. Install Dependencies: The instructions to install the necessary dependencies were included in this Dockerfile(i.e. requirements.txt). Pip was used in this instance to install Python libraries.
3. Exposing Ports:Using the Dockerfile’s EXPOSE directive, we defined the port on which the server will execute.
4. Building the Docker Image: Use the docker build command to create the Docker image. confirming that the required files are there and that the Dockerfile is within the build’s context.
5. Creating requirements file: This guarantees that your application’s dependencies are kept isolated from the Python installation on the whole system. Installing the dependencies for the server within the virtual environment.
The ”requirements.txt” file, which contains a list of all the necessary Python packages and their versions, is created using pip.
6. Docker Hub Repository The Docker file was created and then uploaded to Dockerhub Repository. From there, it was deployed onto ”Azure Container Instances”.
7. Creating a Container Instance: A Container Instance was created in Azure Cloud with the connection made at Dockerhub and the port number specified. Here, the Container Instance created, accessed the Docker image.
8. Server hosting on Cloud: After completing the ensuing procedures, the server was successfully deployed on Azure Cloud (Container Instance). After successfull
deployment,”FQDN”, this URL is generated in container instance, which is used in the code to access the server.As the client requested the data, we observed the spikes in this instance.
