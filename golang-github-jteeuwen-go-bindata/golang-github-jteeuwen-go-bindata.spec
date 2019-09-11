#
# spec file for package golang-github-jteeuwen-go-bindata
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           golang-github-jteeuwen-go-bindata
Version:        3.0.7+git20151023.72.a0ff256
Release:        0
Summary:        A small utility which generates Go code from any file
License:        CC0-1.0
Group:          Development/Languages/Golang
Url:            https://github.com/jteeuwen/go-bindata
Source:         go-bindata-v%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  xz
Provides:       go-bindata = %{version}
Obsoletes:      go-bindata < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}
Provides:       golang(github.com/jteeuwen/go-bindata)
ExcludeArch:    s390

%description
This package converts any file into manageable Go source code. Useful for embedding binary data into a go program. The file data is optionally gzip compressed before being converted to a raw byte slice.

It comes with a command line tool in the go-bindata sub directory. This tool offers a set of command line options, used to customize the output being generated.

%prep
%setup -q -n go-bindata-v%{version}

%build
%{goprep} github.com/jteeuwen/go-bindata
%{gobuild} ...

%install
%{goinstall}
%if 0%{?go_filelist:1} > 0
 %{go_filelist}
%else
 %{gofilelist}
%endif

%check
%{gotest} github.com/jteeuwen/go-bindata

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
/usr/bin/go-bindata

%changelog
