#
# spec file for package apptainer
#
# Copyright (c) 2022 SUSE LLC
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


%define apptainerpath src/github.com/apptainer/
%define _buildshell /bin/bash

#%%define vers_suffix -rc.2

Summary:        Application and environment virtualization
License:        BSD-3-Clause-LBNL
Group:          Productivity/Clustering/Computing
Name:           apptainer
Version:        1.0.3
Release:        0
# https://spdx.org/licenses/BSD-3-Clause-LBNL.html
URL:            https://apptainer.org
Source0:        https://github.com/apptainer/apptainer/archive/v%{version}%{?vers_suffix}/apptainer-%{version}%{?vers_suffix}.tar.gz
Source1:        README.SUSE
Source2:        SLE-12SP5.def
Source3:        SLE-15SP3.def
Source5:        %{name}-rpmlintrc
Source10:       vendor.tar.gz
Patch1:         useful_error_message.patch
BuildRequires:  cryptsetup
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  go >= 1.17
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sysuser-tools
%ifarch aarch64
BuildRequires:  binutils-gold
%endif
BuildRequires:  libseccomp-devel
Requires:       squashfs
PreReq:         permissions

# there's no golang for ppc64, ppc64le does not have non pie builds
ExcludeArch:    ppc64 ppc64le

Provides:       %{name}-runtime
Obsoletes:      singularity
Obsoletes:      singularity-runtime

%description
Singularity provides functionality to make portable
containers that can be used across host environments.

%prep
%setup -q -n gopath/%{apptainerpath} -c
cp %{S:1} %{S:2} %{S:3} .
mv %{name}-%{version}%{?vers_suffix} %{name}
cd %{_builddir}/gopath/%{apptainerpath}/apptainer
%patch1 -p1

%build
cd %{name}
# create VERSION file
echo %version > VERSION
# Not all of these parameters currently have an effect, but they might be
#  used someday.  They are the same parameters as in the configure macro.
tar xzf %{S:10}
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
export GOFLAGS=-mod=vendor
export PATH=$GOPATH/bin:$PATH
cd %{name}/builddir

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make DESTDIR=$RPM_BUILD_ROOT install man
cd ../..
%fdupes apptainer/examples
mkdir -p .tmp
for j in LICENSE.md LICENSE; do
    for i in `find . -name $j`; do
      k="`basename ${i/%\/$j/-$j}`"
      if ! [[ $k =~ apptainer-.* ]]; then
          cp $i .tmp/$k
      fi
    done
done

echo "g %name -" > system-group-%{name}.conf
%sysusers_generate_pre system-group-%{name}.conf %{name} system-group-%{name}.conf
install -D -m 644 system-group-%{name}.conf %{buildroot}%{_sysusersdir}/system-group-%{name}.conf

%fdupes -s .tmp
mv .tmp/* .
rmdir .tmp

%pre -f %{name}.pre

%post
%set_permissions %{_libexecdir}/apptainer/bin/starter-suid

%verifyscript
%set_permissions %{_libexecdir}/apptainer/bin/starter-suid

%files
%doc apptainer/examples
%doc apptainer/CONTRIBUTING.md
%doc apptainer/README.md
%doc apptainer/CHANGELOG.md
%doc apptainer/CONTRIBUTORS.md
%doc %{basename:%{S:1}}
%doc %{basename:%{S:2}}
%doc %{basename:%{S:3}}
%license apptainer/LICENSE.md
%license *-LICENSE.md *-LICENSE
%attr(4750, root, apptainer) %{_libexecdir}/apptainer/bin/starter-suid
%{_bindir}/*
%dir %{_libexecdir}/apptainer
%dir %{_libexecdir}/apptainer/bin
%dir %{_libexecdir}/apptainer/cni
%{_libexecdir}/apptainer/bin/starter
%{_libexecdir}/apptainer/cni/*
%dir %{_sysconfdir}/apptainer
%config(noreplace) %{_sysconfdir}/apptainer/capability.json
%config(noreplace) %{_sysconfdir}/apptainer/cgroups
%config(noreplace) %{_sysconfdir}/apptainer/ecl.toml
%config(noreplace) %{_sysconfdir}/apptainer/global-pgp-public
%config(noreplace) %{_sysconfdir}/apptainer/network
%config(noreplace) %{_sysconfdir}/apptainer/nvliblist.conf
%config(noreplace) %{_sysconfdir}/apptainer/seccomp-profiles
%config(noreplace) %{_sysconfdir}/apptainer/apptainer.conf
%config(noreplace) %{_sysconfdir}/apptainer/remote.yaml
%config(noreplace) %{_sysconfdir}/apptainer/rocmliblist.conf
%config(noreplace) %{_sysconfdir}/apptainer/dmtcp-conf.yaml
%{_datadir}/bash-completion/completions/*
%dir %{_localstatedir}/lib/apptainer
%dir %{_localstatedir}/lib/apptainer/mnt
%dir %{_localstatedir}/lib/apptainer/mnt/session
%{_mandir}/man1/*
%{_sysusersdir}/system-group-%{name}.conf

%changelog
