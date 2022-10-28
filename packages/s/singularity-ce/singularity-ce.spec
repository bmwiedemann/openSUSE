#
# spec file for package singularity-ce
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2022, SyLabs, Inc. All rights reserved.
# Copyright (c) 2017, SingularityWare, LLC. All rights reserved.
# Copyright (c) 2015-2017, Gregory M. Kurtzer. All rights reserved.
# Copyright (c) 2016, The Regents of the University of California, through
# Lawrence Berkeley National Laboratory (subject to receipt of any required
# approvals from the U.S. Dept. of Energy).  All rights reserved.
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


%undefine _debugsource_packages
# will define the singularity group for comaptibilty to non community version
%define noncename singularity

Summary:        Application and environment virtualization
Name:           singularity-ce
Version:        3.10.2
Release:        0
License:        Apache-2.0 AND BSD-3-Clause-LBNL
URL:            https://www.sylabs.io/singularity/
Provides:       singularity
Obsoletes:      singularity <= 3.8.5
Source:         https://github.com/sylabs/singularity/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Patch1:         useful_error_message.patch
ExclusiveOS: linux

BuildRequires:  cryptsetup
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  go
BuildRequires:  libseccomp-devel
BuildRequires:  make
BuildRequires:  sysuser-tools

Requires:       cryptsetup
Requires:       runc
%if "%{_target_vendor}" == "suse"
Requires:       squashfs
%else
Requires:       libseccomp
Requires:       squashfs-tools
%endif
PreReq:         permissions

# there's no golang for ppc64, just ppc64le
ExcludeArch:    ppc64

Provides:       %{name}-runtime

# Conflicts with non-CE packages
Conflicts:      singularity
# Conflicts with Apptainer, which installs the `/usr/bin/singularity` compatibility executable
Conflicts:      apptainer
# Conflicts with SingularityPRO basic packaging (not other variants).
Conflicts:      singularitypro24
Conflicts:      singularitypro25
Conflicts:      singularitypro26
Conflicts:      singularitypro31
Conflicts:      singularitypro35
Conflicts:      singularitypro37
Conflicts:      singularitypro39

%description
SingularityCE is the Community Edition of Singularity, an open source
container platform designed to be simple, fast, and secure.

%prep
# Extract the source
%setup  -q -n %{name}-%{version}
cp %{S:1} .
%patch1 -p1

%build
# Setup an empty GOPATH for the build
export GOPATH=$PWD/gopath
mkdir -p "$GOPATH"
# remove stray binary https://github.com/sylabs/singularity/issues/941
rm third_party/conmon/bin/conmon

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
        --localstatedir=%{_localstatedir}/lib/ \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \

make -C builddir old_config=

%install
export GOPATH=$PWD/gopath

make -C builddir DESTDIR=%{buildroot} install

# cleanup stuff
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/

echo "g %noncename -" > system-group-%{name}.conf
%sysusers_generate_pre system-group-%{name}.conf %{name} system-group-%{name}.conf
install -D -m 644 system-group-%{name}.conf %{buildroot}%{_sysusersdir}/system-group-%{name}.conf

%pre -f %{name}.pre

%post
%set_permissions %{_libexecdir}/singularity/bin/starter-suid

%verifyscript
%set_permissions %{_libexecdir}/singularity/bin/starter-suid

%files
%attr(4750, root, %noncename)  %{_libexecdir}/singularity/bin/starter-suid
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/singularity
%{_libexecdir}/singularity/cni
%{_libexecdir}/singularity/bin
%{_libexecdir}/singularity/bin/starter
%{_libexecdir}/singularity/cni/*
%dir %{_sysconfdir}/singularity
%dir %{_sysconfdir}/singularity/cgroups
%dir %{_sysconfdir}/singularity/network
%dir %{_sysconfdir}/singularity/seccomp-profiles
%config(noreplace) %{_sysconfdir}/singularity/*.conf
%config(noreplace) %{_sysconfdir}/singularity/*.toml
%config(noreplace) %{_sysconfdir}/singularity/*.json
%config(noreplace) %{_sysconfdir}/singularity/*.yaml
%config(noreplace) %{_sysconfdir}/singularity/global-pgp-public
%config(noreplace) %{_sysconfdir}/singularity/cgroups/*
%config(noreplace) %{_sysconfdir}/singularity/network/*
%config(noreplace) %{_sysconfdir}/singularity/seccomp-profiles/*
%dir %{_sysconfdir}/bash_completion.d
%{_datadir}/bash-completion/completions/*
%dir %{_localstatedir}/lib/singularity
%dir %{_localstatedir}/lib/singularity/mnt
%dir %{_localstatedir}/lib/singularity/mnt/session
%{_mandir}/man1/singularity*
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%doc %{basename:%{S:1}}
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc CONTRIBUTORS.md
%{_sysusersdir}/system-group-%{name}.conf

%changelog
