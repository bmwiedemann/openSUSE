#
# spec file for package golang-github-nsf-gocode
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%global _name godef
%global _devname rogpeppe
Name:           golang-github-%{_devname}-%{_name}
Version:        0+git.1466415558.ee532b9
Release:        0
License:        BSD-3-Clause
Summary:        Find symbol information in Go source
Url:            https://github.com/%{_devname}/%{_name}
Group:          Development/Languages/Golang
Source0:        %{_name}-%{version}.tar.xz
Source1:        %{_name}.1
BuildRequires:  golang-packaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}

%description
Godef, given an expression or a location in a source file, prints the
location of the definition of the symbol referred to.


%prep
%setup -q -n %{_name}-%{version}

%build
%goprep github.com/%{_devname}/%{_name}
%gobuild ...

%install
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{_sourcedir}/%{_name}.1 %{buildroot}%{_mandir}/man1/%{_name}.1
%goinstall
%gosrc
rm -rvf %{buildroot}/%{_libdir}

%gofilelist

%files -f file.lst
%defattr(-,root,root)
%doc LICENSE README
%{_mandir}/man1/*
%{_bindir}/godef

%changelog

