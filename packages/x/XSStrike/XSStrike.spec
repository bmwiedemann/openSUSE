#
# spec file for package python-xsstrike
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           XSStrike
Version:        3.1.5
Release:        0
Summary:        Most advanced XSS scanner
License:        GPL-3.0-only
URL:            https://github.com/s0md3v/XSStrike
Source:         XSStrike-3.1.5.tar.gz
Patch0:         fix_shebang.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python3-fuzzywuzzy
BuildArch:      noarch

%description

XSStrike is a Cross Site Scripting detection suite equipped with four hand
written parsers, an intelligent payload generator, a powerful fuzzing engine
and an incredibly fast crawler.

Instead of injecting payloads and checking it works like all the other tools
do, XSStrike analyses the response with multiple parsers and then crafts
payloads that are guaranteed to work by context analysis integrated with a
fuzzing engine.


%prep
%setup -q -n XSStrike-%{version}
%patch0 -p1

%build

%install
mkdir -p %{buildroot}/usr/share/xsstrike
chmod ugo+x xsstrike.py
cp -a * %{buildroot}/usr/share/xsstrike

%python_expand %fdupes %{buildroot}/usr/share/xsstrike

%post
%{__ln_s} -f  /usr/share/xsstrike/xsstrike.py %{_bindir}

%postun
case "$1" in
  0) # last one out put out the lights
    rm -f %{_bindir}/xsstrike.py
  ;;
esac

%files
/usr/share/xsstrike

%license /usr/share/xsstrike/LICENSE
%doc /usr/share/xsstrike/README.md

%changelog
