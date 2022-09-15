From upstream releases, choose the file with `helix-<version>-source.tar.xz`.
And run `rpmdev-spectool -g helix.spec`. Create a directory named `helix` where
you should extract the contents of the downloaded tarball. Thereafter, run
`osc service disabledrun`. This will run cargo vendor and compress them inside
a tarball. You can check if you want to disable the cargo update mechanism.

Please do remember to create separate packages for the runtime and the helix 
binary as the former is huge when built. Helix still runs fine without 
the runtime but for it to run "normally" a user just needs to run 
`helix --grammar fetch` then `helix --grammar build`. The purpose of the 
runtime files as a package is to maintain consistency and convenience 
and stay faithful with how other packagers do it and when someone needs it.
