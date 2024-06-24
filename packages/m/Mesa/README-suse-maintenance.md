Since Rust crates are not installed or discouraged to be installed
as system dependencies because of the maintenance burden of being the
next crates.io, we will have to download the following crates as vendored
dependencies. Hence, do not be scared if the dependencies are done like
this.

To check new crates or update the versions, just go to the subprojects
folder and run `grep -r crates .` then set versions appropriately.
