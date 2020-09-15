#
# spec file for package singularity
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define singgopath src/github.com/sylabs/
%define _buildshell /bin/bash

Summary:        Application and environment virtualization
License:        BSD-3-Clause-LBNL
Group:          Productivity/Clustering/Computing
Name:           singularity
Version:        3.6.2
Release:        0
# https://spdx.org/licenses/BSD-3-Clause-LBNL.html
URL:            https://github.com/hpcng/singularity
Source0:        https://github.com/hpcng/singularity/releases/download/v%{version}/singularity-%{version}.tar.gz
Source1:        README.SUSE
Source5:        %{name}-rpmlintrc
Patch1:         useful_error_message.patch
BuildRequires:  cryptsetup
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  go1.13
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
%ifarch aarch64
BuildRequires:  binutils-gold
%endif
Requires:       squashfs
PreReq:         permissions

# there's no golang for ppc64, just ppc64le
ExcludeArch:    ppc64

Provides:       %{name}-runtime

%description
Singularity provides functionality to make portable
containers that can be used across host environments.


%prep
%setup -q -n gopath/%{singgopath} -c
%patch1 -p 4
cp %{S:1} .

%build
export GOPATH=$PWD/gopath
export PATH=$GOPATH/bin:$PATH
cd %{name}

# Not all of these parameters currently have an effect, but they might be
#  used someday.  They are the same parameters as in the configure macro.
./mconfig -V %{version}-%{release} \
        -P release \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir}/lib \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir}
cd builddir
make V="" old_config=

%install
export GOPATH=$PWD/gopath
export PATH=$GOPATH/bin:$PATH
cd %{name}/builddir

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make DESTDIR=$RPM_BUILD_ROOT install man
# move bash completion to the right place
mkdir -pv %{buildroot}/%{_datadir}/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/singularity \
	%{buildroot}/%{_datadir}/bash-completion/completions/
cd ../..
%fdupes singularity/examples
mkdir -p .tmp
for j in LICENSE.md LICENSE; do
    for i in `find . -name $j`; do
	k="`basename ${i/%\/$j/-$j}`"
	if ! [[ $k =~ singularity-.* ]]; then
	    cp $i .tmp/$k
	fi
    done
done
%fdupes -s .tmp
mv .tmp/* .
rmdir .tmp

%pre 
getent group singularity >/dev/null || groupadd -r singularity
exit 0

%post 
%set_permissions %{_libexecdir}/singularity/bin/starter-suid

%verifyscript
%set_permissions %{_libexecdir}/singularity/bin/starter-suid

%files
%doc singularity/examples
%doc singularity/CONTRIBUTING.md
%doc singularity/README.md
%doc singularity/CHANGELOG.md
%doc singularity/CONTRIBUTORS.md
%doc %{basename:%{S:1}}
%license singularity/LICENSE-LBNL.md
%license singularity/COPYRIGHT.md
%license singularity/LICENSE.md
%license *-LICENSE.md *-LICENSE
%attr(4750, root, singularity) %{_libexecdir}/singularity/bin/starter-suid
%{_bindir}/*
%dir %{_libexecdir}/singularity
%dir %{_libexecdir}/singularity/bin
%dir %{_libexecdir}/singularity/cni
%{_libexecdir}/singularity/bin/starter
%{_libexecdir}/singularity/cni/*
%dir %{_sysconfdir}/singularity
%config(noreplace) %{_sysconfdir}/singularity/capability.json
%config(noreplace) %{_sysconfdir}/singularity/cgroups
%config(noreplace) %{_sysconfdir}/singularity/ecl.toml
%config(noreplace) %{_sysconfdir}/singularity/network
%config(noreplace) %{_sysconfdir}/singularity/nvliblist.conf
%config(noreplace) %{_sysconfdir}/singularity/seccomp-profiles
%config(noreplace) %{_sysconfdir}/singularity/singularity.conf
%config(noreplace) %{_sysconfdir}/singularity/remote.yaml
%config(noreplace) %{_sysconfdir}/singularity/rocmliblist.conf
%{_datadir}/bash-completion/completions/singularity
%dir %{_localstatedir}/lib/singularity
%dir %{_localstatedir}/lib/singularity/mnt
%dir %{_localstatedir}/lib/singularity/mnt/session
%{_mandir}/man1/*

%changelog
