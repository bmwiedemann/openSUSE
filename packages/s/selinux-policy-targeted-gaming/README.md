# selinux-policy-gaming

SELinux policy changes for a simplified gaming experience

## Intention

Provide a simple way for packagers to allow gaming related changes to the
installed selinux policy, while still providing a central point to track and
evolve the changes needed for gaming on Linux.

The goal is to learn over time what these requirements are and improve the 
security of these changes over time.

## Details

The package makes the following change to the system during package install:

> semanage boolean -m --on selinuxuser_execmod
> semanage boolean -m --on selinuxuser_execstack
> semanage boolean -m --on selinuxuser_execheap

or identical change, but using another tool

> setsebool -P selinuxuser_execmod 1
> setsebool -P selinuxuser_execstack 1
> setsebool -P selinuxuser_execheap 1

This change has security implications, as it allows unconfined executables to
make their stack executable. Usually because certain libraries requiring text
relocation.

In the past administrator had to make the change manually on the system,
see https://en.opensuse.org/Portal:SELinux/Common_issues#Steam_Proton,_Bottles,_WINE,_Lutris,_not_working
