#
# spec file for package gyp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nurenberg, Germany.
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


Name:           gyp
Version:        0+git.20171012
Release:        0
Summary:        Generate Your Projects
License:        BSD-3-Clause
Group:          Development/Tools/Building
Url:            https://gyp.gsrc.io
Source:         %{name}-%{version}.tar.xz
Patch0:         gyp-rpmoptflags.patch
BuildRequires:  fdupes
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-setuptools
BuildArch:      noarch

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons and/or make
build files from a platform-independent input format. Its syntax is a universal
cross-platform build representation that still allows sufficient per-platform
flexibility to accommodate irreconcilable differences

%prep
%setup -q
%patch0
for i in $(find pylib -name '*.py'); do
	sed -e '\,#![ \t]*/.*python,{d}' $i > $i.new && touch -r $i $i.new && mv $i.new $i
done
sed -i '/^#!/d' ./pylib/%{name}/*.py
sed -i '/^#!/d' ./pylib/%{name}/generator/*.py

%build
python2 setup.py build

%install
python2 setup.py install --root %{buildroot} --prefix=%{_prefix}
%fdupes -s %{buildroot}%{python_sitelib}

%files
%doc AUTHORS LICENSE
%{_bindir}/%{name}
%{python_sitelib}/*

%changelog
