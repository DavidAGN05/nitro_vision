FROM dustynv/ros:jazzy-desktop-r36.4.0-cu128-24.04

# Arguments for user creation
ARG USERNAME=david
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update \
    && apt-get install -y sudo \
    && echo ubuntu ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ubuntu \
    && chmod 0440 /etc/sudoers.d/ubuntu

# Install extra dependencies (add more as needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python-is-python3 \
        libopencv-dev \
        libboost-all-dev \
        openssl \
        git \
        gdb \
        libi2c-dev \
        i2c-tools \
        libcurl4-openssl-dev \
        libssl-dev \
        curl \
        ros-jazzy-imu-tools \
        ros-jazzy-teleop-twist-joy \
        ros-jazzy-image-transport \
        ros-jazzy-desktop \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/jazzy/setup.bash" >> /etc/bash.bashrc && \
    echo "source /opt/ros/jazzy/setup.bash" >> /home/ubuntu/.bashrc

USER ubuntu

# (Optional) Install Node.js as in your turtlesim example
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# ENV NVM_DIR=/home/$USERNAME/.nvm \
#     NODE_VERSION=20.10.0
# RUN . $NVM_DIR/nvm.sh \
#     && nvm install $NODE_VERSION \
#     && nvm alias default $NODE_VERSION \
#     && nvm use default

USER root

ENTRYPOINT ["./ros_entrypoint.sh"]
CMD [ "bash" ]
