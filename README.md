This repo is a public read-only git mirror of openSUSE sources
from [build.opensuse.org](https://build.opensuse.org/).

Advantages are:

* easy to do full-text search
* offline access to history
* Git blame is fast, both online and offline.
* distributed repo
* increased visibility of changes
* also tracks prjconf changes
* ability to download patch files
* cryptographically signed commits to impede tampering with history
* even works on Thursdays (when we do maintenance of our infrastructure)
* does not carry tarballs and other large binaries, so the whole repo is still below 1GB

Binary files are replaced by cryptographically secure symlinks into IPFS. 
If you can not run ipfs, you can still get these files through any of the public gateways like this:
`curl https://ipfs.io$(readlink packages/a/aubio/aubio-0.4.9.tar.bz2) > OUTPUT`
