# SLE BCI-Micro: Suitable for deploying static binaries

This image is similar to SLE BCI-Minimal but without the RPM package manager.
The primary use case for the image is deploying static binaries produced
externally or during multi-stage builds. As there is no straightforward
way to install additional dependencies inside the container image,
we recommend deploying a project using the SLE BCI-Minimal image only
when the final build artifact bundles all dependencies and has no
external runtime requirements (like Python or Ruby).

## License
 SPDX-License-Identifier: MIT