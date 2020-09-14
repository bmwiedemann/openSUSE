#
# spec file for package apache-rex
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


#
%if 0%{?suse_version} > 1230
%define macros_dir            %{_rpmconfigdir}/macros.d
%else
%define macros_dir            %{_sysconfdir}/rpm
%endif
%define macros_file           macros.apache-rex

Name:           apache-rex
Version:        20200901
Release:        0
Summary:        Script for Apache HTTPD Runnable Examples
License:        Apache-2.0
Group:          Documentation/Howto
URL:            https://github.com/pgajdos/apache-rex
Source0:        %{name}.tar.bz2
Source1:        apache-rex-rpmlintrc
Source2:        %{macros_file}
Requires:       apache2-devel
Requires:       curl
Requires:       lsof
Requires:       openssl
Requires:       openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Runnable examples for Apache HTTP server. Can be used starting
point for examples, testcases and other inspiration.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp run-rex %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r */ LICENSE README.md contents %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{macros_dir}
install -m 644 %{SOURCE2} %{buildroot}%{macros_dir}/%{macros_file}

%files
%defattr(-,root,root)
%{_bindir}/run-rex
%{macros_dir}/%{macros_file}
%{_docdir}/%{name}

%changelog
