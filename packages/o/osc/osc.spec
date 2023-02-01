#
# spec file for package osc
#
# Copyright (c) 2023 SUSE LLC
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


%define use_python python3
%define use_python_pkg python3

%if 0%{?suse_version} && 0%{?suse_version} < 1500
# use python36 on SLE 12 and older
%define use_python python3.6
%define use_python_pkg python36
%endif

%define completion_dir_bash %{_datadir}/bash-completion/completions
%define completion_dir_csh %{_sysconfdir}/profile.d
%define completion_dir_fish %{_datadir}/fish/vendor_completions.d
%define osc_plugin_dir %{_prefix}/lib/osc-plugins
# need to override python_sitelib because it is not set as we would expect on many distros
%define python_sitelib %(RPM_BUILD_ROOT= %{use_python} -Ic "import sysconfig; print(sysconfig.get_path('purelib'))")

%if 0%{?is_opensuse}
%define completion_dir_bash %{_sysconfdir}/bash_completion.d
%endif

# generate manpages on distros where argparse-manpage >= 3 is available
%if 0%{?suse_version} > 1500 || 0%{?fedora} >= 37
%bcond_without man
%else
%bcond_with man
%endif

%define argparse_manpage_pkg %{use_python_pkg}-argparse-manpage
%if 0%{?fedora}
%define argparse_manpage_pkg argparse-manpage
%endif

Name:           osc
Version:        1.0.0~b3
Release:        0
Summary:        Command-line client for the Open Build Service
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/osc

Source:         %{name}-%{version}.tar.gz

%if 0%{?debian}
Source1:        debian.dirs
Source2:        debian.docs
%endif
Patch1:         https://github.com/openSUSE/osc/pull/1228.patch
Patch2:         https://github.com/openSUSE/osc/pull/1217.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if %{with man}
BuildRequires:  %{argparse_manpage_pkg}
%endif
BuildRequires:  %{use_python_pkg}-cryptography
BuildRequires:  %{use_python_pkg}-devel >= 3.6
BuildRequires:  %{use_python_pkg}-rpm
BuildRequires:  %{use_python_pkg}-setuptools
BuildRequires:  %{use_python_pkg}-urllib3
BuildRequires:  diffstat

Requires:       %{use_python_pkg}-cryptography
Requires:       %{use_python_pkg}-rpm
Requires:       %{use_python_pkg}-urllib3

# needed for showing download progressbars
Recommends:     %{use_python_pkg}-progressbar

# needed for storing credentials in kwallet/gnome-keyring
Recommends:     %{use_python_pkg}-keyring
Recommends:     %{use_python_pkg}-keyring-keyutils

Recommends:     build
Recommends:     ca-certificates
Recommends:     diffstat
Recommends:     powerpc32
Recommends:     sudo

# needed for `osc add <URL>`
Recommends:     obs-service-recompress
Recommends:     obs-service-download_files
Recommends:     obs-service-format_spec_file
Recommends:     obs-service-obs_scm
Recommends:     obs-service-set_version
Recommends:     obs-service-source_validator
Recommends:     obs-service-tar_scm
Recommends:     obs-service-verify_file

%if 0%{?fedora}
Recommends:     openssh
%endif
%if 0%{?suse_version}
Recommends:     openssh-common
%endif

# needed for `osc browse` that calls xdg-open
Recommends:     xdg-utils

Provides:       %{use_python_pkg}-osc

%description
OpenSUSE Commander is a command-line client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC, as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial
for a general introduction.

%prep
%autosetup -p1

%build
%{use_python} setup.py build

# write rpm macros
cat << EOF > macros.osc
%%osc_plugin_dir %{osc_plugin_dir}
EOF

# build man page
%if %{with man}
PYTHONPATH=. argparse-manpage \
    --output=osc.1 \
    --format=single-commands-section \
    --module=osc.commandline \
    --function=get_parser \
    --project-name=osc \
    --prog=osc \
    --description="OpenSUSE Commander" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"
%endif

%install
%{use_python} setup.py install -O1 --skip-build --force --root %{buildroot} --prefix %{_prefix}

# create plugin dirs
install -d %{buildroot}%{osc_plugin_dir}
install -d %{buildroot}%{_sharedstatedir}/osc-plugins

# install completions
install -Dm0755 contrib/osc.complete %{buildroot}%{_datadir}/osc/complete
install -Dm0644 contrib/complete.csh %{buildroot}%{completion_dir_csh}/osc.csh
install -Dm0644 contrib/complete.sh %{buildroot}%{completion_dir_bash}/osc.sh
install -Dm0644 contrib/osc.fish %{buildroot}%{completion_dir_fish}/osc.fish

# install rpm macros
install -Dm0644 macros.osc %{buildroot}%{_rpmmacrodir}/macros.osc

# install man page
%if %{with man}
install -Dm0644 osc.1 %{buildroot}%{_mandir}/man1/osc.1
%endif

%check
%{use_python} setup.py test

%files
%defattr(-,root,root,-)

# docs
%license COPYING
%doc AUTHORS README.md NEWS
%if %{with man}
%{_mandir}/man1/osc.*
%endif

# executables
%{_bindir}/*

# python modules
%{python_sitelib}/*

# rpm macros
%{_rpmmacrodir}/*

# plugins
%dir %{osc_plugin_dir}
%dir %{_sharedstatedir}/osc-plugins

# completions
%dir %{_datadir}/osc
%{_datadir}/osc/complete
%{completion_dir_bash}/*
%{completion_dir_csh}/*
%{completion_dir_fish}/*

# osc owns the dirs to avoid the "directories not owned by a package" build error
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d

%changelog
