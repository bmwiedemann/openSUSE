# SLE BCI-Minimal: Container image without Zypper

SLE BCI-Minimal comes without Zypper, but it does have the RPM package manager installed. While RPM can install and remove packages, it lacks support for repositories and automated dependency resolution. The SLE BCI-Minimal image is therefore intended for creating deployment containers, and then installing the desired RPM packages inside the containers. While you can install the required dependencies, you need to download and resolve them manually. However, this approach is not recommended as it is prone to errors.

## License
 SPDX-License-Identifier: MIT