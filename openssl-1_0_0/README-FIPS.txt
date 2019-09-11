README-FIPS.txt - Roman Drahtmueller <draht@suse.de>, June 16 2012

NOTE: Finished the adjustment of DSO path and correct the version
information for SLE 12. Still need to review about AES-NI optimization.
Shawn Chang <shchang@suse.com>, Dec 7 2013.

NOTE: Outdated currently for openSUSE Factory / SLE 12, needs review
and adjustments. But basic settings still are the same.
Marcus Meissner <meissner@suse.de>, 2013/Dec/03.

* general information
* FIPS-140-2 mode of operation
* overview: openssl subpackages on SLES12
==============================================================================



* general information
==============================================================================

Dear user of the SUSE Linux Enterprise Server,

SLES12 comes with openssl of version 1.0.1e, a version upgrade from
0.9.8j that came with earlier revisions of SLES11-SP3.

The new version has support for FIPS-140-2 mode of operation.
FIPS is short for Federal Information Processing Standard.
For more information on FIPS-140-2, please see
http://csrc.nist.gov/publications/fips/fips140-2/fips1402.pdf
and more publications on the NIST website.

The openssl shared libraries are used by numerous packages in the
SUSE Linux Enterprise Server. If the library runs in FIPS-140-2 mode,
then the binary that links against the library at runtime makes use
of FIPS-140-2 validated cryptography as defined in its cryptographic
module. By consequence, a large number of packages can make a claim
about using FIPS-140-2 validated cryptographical functions.

Both the 64bit and the 32bit shared libraries are supported in FIPS-140-2
mode of operation.
Both in 64bit and in 32bit mode, the AES-NI assembler optimizations are
supported and used, if the used CPU supports the AES-NI instructions. These
assembler optimizations can deliver a substantial performance benefit.
To check if your system's CPU(s) has (have) AES-NI support, have a look 
into the Linux kernel's /proc file /proc/cpuinfo - search it for the "aes"
flag.
AES-NI support can be disabled by setting the environment variable
OPENSSL_DISABLE_AESNI before running binaries that link against openssl.
The "openssl speed" command can give you an idea for the performance
differences.


The cryptographic module as defined for FIPS-140-2 is contained in the files
   /lib64/.libcrypto.so.1.0.0.hmac
   /lib64/.libssl.so.1.0.0.hmac
   /lib64/libcrypto.so.1.0.0
   /lib64/libssl.so.1.0.0
for 64bit operation and
   /lib/.libcrypto.so.1.0.0.hmac
   /lib/.libssl.so.1.0.0.hmac
   /lib/libcrypto.so.1.0.0
   /lib/libssl.so.1.0.0
for 32bit.

  The .hmac files contain a HMAC for the internal integrity checking. They 
are contained in the package libopenssl1_0_0-hmac, seperate from the 
libopenssl1_0_0 package. These hashes are produced as one of the last steps 
during the RPM build process.
  If the library starts up in FIPS mode, the .hmac files are read, and the 
checksum is verified against a new self-measurement of the library. 
Essentially, this means that the FIPS mode of operation is not possible
without the .hmac files from the corresponding -hmac package installed.
  If the library starts up in non-FIPS mode, it checks if the .hmac files 
exist, and if so, it runs through the self-tests as if it operates in FIPS 
mode. This self-test in non-FIPS mode is formally mandatory and comes with
a heavy CPU footprint. You can avoid this overhead by un-installing the 
libopenssl1_0_0-hmac package (with the consequence that FIPS mode of 
operation becomes unavailable).

The openssl library operates in non-FIPS mode by default.


* FIPS-140-2 mode of operation
==============================================================================

The openssl library operates in non-FIPS mode by default. 

As noted above (* general information), the .hmac files for the integrity 
self-check of the openssl library are contained in their own package. 
Unfortunately, the self-test is mandatory even if the library runs in 
non-FIPS mode, causing a significant CPU consumption during openssl's 
initialization. You can avoid this overhead by de-installing the -hmac 
package if you do not need FIPS mode of operation.

If you DO need to run binaries that are linked against the openssl 
cryptographic library that runs in FIPS mode, you MUST have the 
libopenssl1_0_0-hmac package installed.

!!! If you enable FIPS mode of operation with the methods below, you MUST 
!!! have the libopenssl1_0_0-hmac package installed. Programs that runtime-link 
!!! against openssl will abort if the FIPS self-tests (including the 
!!! integrity check with the .hmac hashes) fail!

There are three ways to switch the shared libraries listed above to
FIPS-140-2 compliant mode:

1) Start your system with the kernel commandline option "fips=1". To
   change the configuration for your system on a permanent basis, please
   add the command line option to the corresponding line in the bootloader
   configuration, typically /boot/grub/menu.lst .
   You can check if the kernel has accepted the commandline option at boot
   by inspecting the content of the file /proc/sys/crypto/fips_enabled .
     Please note that the fips=1 kernel commandline option switches
   the kernel's crypto API to FIPS mode operation, too. As a consequence,
   some of the in-kernel cryptographical functions may become unavailable.
     As of the writing of this README-FIPS.txt, the kernel's crypto API in
   the SUSE Linux Enterprise Server was NOT FIPS-140-2 validated!


2) set the environment variable OPENSSL_FORCE_FIPS_MODE to "1":

	export OPENSSL_FORCE_FIPS_MODE=1

   and run your application with this environment variable set.
   The FIPS-140-2 mode of operation is only given in the context of
   processes that have OPENSSL_FORCE_FIPS_MODE set, unless the global
   switch as in 1) above is active.


3) In your program, use the exported function

	int FIPS_mode_set(int onoff);

   to turn on FIPS-140-2 compliant mode. The library will conduct the
   mandatory self-tests and the integrity check that makes use of the
   .hmac files mentioned above.
   The function

	int FIPS_mode(void);

   can be used to check if the library operates in FIPS-140-2 compliant
   mode. It returns 1 in FIPS mode, 0 otherwise.

Notes:

- An easy way to verify if your openssl cryptography subsystem operates
  in FIPS-140-2 compliant mode is to look at the output of the

	openssl ciphers

  command. In FIPS-140-2 compliant mode, the output lists fewer
  algorythms.

- The startup time of programs that initialize the openssl shared libraries
  in FIPS-140-2 compliant mode is considerably longer due to the self-tests
  that are being executed. On fast systems, the startup overhead can be in the 
  range of 0.05-0.3s. The startup time is two orders of a magnitude smaller
  in non-FIPS mode.
  Please note that the self-test overhead only occurs during the 
  initialization of the cryptographic module. There is no other 
  performance impact of FIPS-140-2 compliant operation of the library.

- The environment variable OPENSSL_FIPS can be set to force the 
  /usr/bin/openssl binary to operate in FIPS-140-2 compliant mode:

	OPENSSL_FIPS=1 openssl ciphers

  The variable OPENSSL_FIPS has an effect on the openssl binary only.

- Services and daemons that make use of the openssl shared libraries in
  FIPS-140-2 compliant mode need to be configured to use algorythms
  from the list of permissable algorythms. If an algorythm is requested
  by an application that is not allowed in FIPS-140-2 compliant mode,
  the application will terminate (abort(3)).
  Please see the FIPS-140-2 Security Policy document for the openssl
  FIPS module on the SUSE Linux Enterprise Server 11 SP1 from the
  SUSE website at http://www.suse.com/ or the NIST website at 
  http://csrc.nist.gov/ for more details.

- If you have any questions about the FIPS-140-2 compliant mode of openssl,
  please send email to security@suse.com.



* overview: openssl subpackages on SLES12
==============================================================================

The openssl package consists of the following RPM package:

openssl

 - manual pages
 - the /etc/ssl configuration directory
 - the /usr/bin/openssl program
 - /usr/bin/fips_standalone_hmac, the program used to reproduce
   the integrity HMAC that is contained in the package:

libopenssl1_0_0
 - files:
   /lib64/libcrypto.so.1.0.0
   /lib64/libssl.so.1.0.0
   /lib64/engines
   /lib64/engines/libcapi.so
   /lib64/engines/libgmp.so
   /lib64/engines/libgost.so
   /lib64/engines/libpadlock.so

libopenssl1_0_0-hmac
- files:
   /lib64/.libcrypto.so.1.0.0.hmac
   /lib64/.libssl.so.1.0.0.hmac

libopenssl1_0_0-32bit
 - files as in package libopenssl1_0_0, but in /lib/.
   The .so libraries are for the 32bit compatibility mode of the
   openssl library.

libopenssl1_0_0-hmac-32bit
- files as in package libopenssl1_0_0-hmac, but in /lib/.

libopenssl-devel
 - header files and static libraries for compiling applications with the
   openssl library. Please note that running binaries that are statically
   linked against openssl libraries is not supported in terms of FIPS-140-2
   compliance.

openssl-doc
 - more documentation and manual pages.

openssl-debuginfo
openssl-debugsource
 - packages that provide debugging symbols and debugging source code for
   running binaries (dynamically) linked against libopenssl1_0_0 in a
   debugger.

openssl-certs
 - CA certificate collection in /etc/ssl/certs
   The openssl-certs package is not a subpackage of the openssl package,
   but it merely provides CA certificates where the openssl package
   finds them.

