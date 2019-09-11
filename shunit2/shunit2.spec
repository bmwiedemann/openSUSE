#
# spec file for package shunit2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define SHUNIT_HOME  %{_datadir}/shunit2
Name:           shunit2
Version:        2.1.6
Release:        0
Summary:        Test Framework for Bourne Based Shell Scripts
License:        LGPL-2.1
Group:          Development/Languages/Other
Url:            https://github.com/kward/shunit2 
Source0:        %{name}-%{version}.tgz
Source1:        lgpl-2.1.txt
Patch0:         %{name}-gen_test_results.sh.diff
Patch1:         %{name}-examples.diff
BuildRequires:  bash
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.
If you have ever had the desire to write a unit test for a shell
script, shUnit2 can do the job.

%prep
%setup -q
# Use the correct version and overwrite it:
cp %{SOURCE1} doc/LGPL-2.1

%patch0
%patch1

%build
# Add the correct basedir in our script:
sed -i 's#@SHUNIT_HOME@#%{SHUNIT_HOME}#g' bin/gen_test_results.sh
for i in examples/*.sh; do
  sed -i 's#@SHUNIT_HOME@#%{SHUNIT_HOME}#g' $i
done

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{SHUNIT_HOME}

install -m 755 src/shunit2 %{buildroot}%{_bindir}
cp -a lib src  %{buildroot}%{SHUNIT_HOME}

%files
%defattr(-,root,root)
%doc doc/* examples
%{_bindir}/*
%dir %{SHUNIT_HOME}
%dir %{SHUNIT_HOME}/src
%dir %{SHUNIT_HOME}/lib
%{SHUNIT_HOME}/src/*
%{SHUNIT_HOME}/lib/*

%changelog
