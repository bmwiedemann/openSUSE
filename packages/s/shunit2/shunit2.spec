#
# spec file for package shunit2
#
# Copyright (c) 2024 SUSE LLC
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


%define SHUNIT_HOME  %{_datadir}/shunit2
Name:           shunit2
Version:        2.1.8
Release:        0
Summary:        Test Framework for Bourne Based Shell Scripts
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/kward/shunit2
Source:         https://github.com/kward/shunit2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash
BuildRequires:  ksh
BuildRequires:  zsh
BuildArch:      noarch

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.
If you have ever had the desire to write a unit test for a shell
script, shUnit2 can do the job.

%prep
%autosetup

%build
#---source /usr/bin/shunit2 in examples, so no additional path settings are needed to use it:
for i in examples/*.sh; do
  sed -i 's|^. ../shunit2|. shunit2|g' "$i"
done

%install
mkdir -p -m 755 %{buildroot}%{_bindir} %{buildroot}%{SHUNIT_HOME} %{buildroot}%{SHUNIT_HOME}/src
install -m 755 shunit2 %{buildroot}%{_bindir}/%{name}
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{SHUNIT_HOME}/%{name}
cp -a lib %{buildroot}%{SHUNIT_HOME}/
#---compat symlink, older versions resided in src/:
ln -sr %{buildroot}%{SHUNIT_HOME}/%{name} %{buildroot}%{SHUNIT_HOME}/src/%{name}

%check
env SHUNIT_COLOR='none' ./test_runner

%files
%license LICENSE
%doc README.md doc/* examples
%{_bindir}/%{name}
%dir %{SHUNIT_HOME}
%dir %{SHUNIT_HOME}/lib
%dir %{SHUNIT_HOME}/src
%{SHUNIT_HOME}/%{name}
%{SHUNIT_HOME}/src/%{name}
%{SHUNIT_HOME}/lib/*

%changelog
