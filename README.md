# dockergpustats

This project is a reinvention of ideas from: [AllenCellModeling/nvidia-docker-stats](https://github.com/AllenCellModeling/nvidia-docker-stats.git) and [nawafalageel/docker_container_gpu_exporter](https://github.com/nawafalageel/docker_container_gpu_exporter.git). Building upon their work in monitoring system resource usage, this tool allows for GPU process monitoring and adds the ability to retrieve Jupyter Notebook tokens associated with Docker containers using the Colab image.

## About

`dockergpustats` is a Python 3 command-line tool designed to determine GPU utilization of processes within Docker containers by combining information from both `nvidia-smi_` and `docker_` commands.

## Features

- **Jupyter Notebook Tokens**: Retrieves Jupyter Notebook tokens for Docker containers using the Colab image.
- **Per-container resource monitoring**: Tracks system resource usage, including GPU usage, for individual Docker containers. This feature builds on the work of [nawafalageel/docker_container_gpu_exporter](https://github.com/nawafalageel/docker_container_gpu_exporter.git), a Docker Container GPU exporter for Prometheus. The `p2g.sh` script and some program logic were adapted from this repository.
- **Per-notebook resource monitoring**: Tracks system resource usage for each notebook running in a Colab Docker container.

## How it works

The tool uses a bash script to extract all GPU-using processes from the system, matches them with the Docker container processes, and outputs detailed statistics about GPU, CPU, RAM, and more for each container and Jupyter notebook session.

## Installation

### Case 1: Cloning the repository

- Clone the repository:
  ```
  git clone https://github.com/Pichuelectrico/dockergpustats.git
  ```
- Navigate to the project directory and execute the `client.py` file:
  ```
  cd dockergpustats
  python3 client.py
  ```

### Case 2: Installing via PyPI

- Install the package using pip:
  ```
  pip install -i https://test.pypi.org/simple/ dockergpustats
  ```
- Run the command:
  ```
  dockergpustats
  ```

## How to contribute

To contribute, fork the repository and submit a pull request with your changes. Refer to `CONTRIBUTING.md` for more information.
