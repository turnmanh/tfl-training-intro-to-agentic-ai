FROM "mcr.microsoft.com/devcontainers/python:3.11-bullseye"

# Install Rust; required for some dependencies.
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y
RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

# Setup uv for dependency management. 
RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh
ENV UV_LINK_MODE=copy
