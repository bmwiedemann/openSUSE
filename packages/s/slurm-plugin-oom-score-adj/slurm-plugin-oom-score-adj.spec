#
# spec file for package slurm-plugin-oom-score-adj
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

%global flavor @BUILD_FLAVOR@%{nil}

%if "%flavor" != ""
%define name_suff %{?flavor:_%{flavor}}
%endif
Name:           slurm%{?name_suff}-plugin-oom-score-adj
Version:        0.git.1459863392.b27ecfb
Release:        0
Summary:        Slurm spank plugin for OOM killer score advisory
License:        CECILL-C
URL:            https://github.com/edf-hpc/slurm-spank-plugin-oom-score-adj
Source0:        slurm-plugin-oom-score-adj-0.git.1459863392.b27ecfb.tar.gz
Patch0:         change_paths.patch
BuildRequires:  slurm%{?name_suff}-devel
Requires:       slurm%{?name_suff}-plugins
ExcludeArch:   %ix86

%description
This plugin adjusts the Out-of-Memory (OOM) score of the tasks
spawned by Slurm.

%prep
%setup -q -n slurm-plugin-oom-score-adj-%{version}
%autopatch

%build
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/slurm/plugstack.conf.d/
install -D -m644 oom_score_adj.conf %{buildroot}%{_sysconfdir}/slurm/plugstack.conf.d/

%files
%license Licence_CeCILL-C_V1-en.txt 
%{_libdir}/slurm/oom-score-adj.so
%dir %{_sysconfdir}/slurm/plugstack.conf.d/
%config %{_sysconfdir}/slurm/plugstack.conf.d/oom_score_adj.conf

%changelog
