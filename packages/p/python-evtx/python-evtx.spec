#
# spec file for package python-evtx
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define commands dump dump_chunk_slack eid_record_numbers extract_record filter_records info record_structure structure templates
%bcond_without python2
Name:           python-evtx
Version:        0.7.4
Release:        0
Summary:        Windows Event Log files parser
License:        Apache-2.0
URL:            https://github.com/williballenthin/python-evtx
Source:         https://github.com/williballenthin/python-evtx/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module hexdump}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
%if %{with python2}
BuildRequires:  python2-xml
%endif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-hexdump
Requires:       python-lxml
Requires:       python-six
%ifpython2
Requires:       python-xml
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
python-evtx is a pure Python parser for recent Windows Event Log files (those
with the file extension ".evtx"). The module provides programmatic access to the
File and Chunk headers, record templates, and event entries. For example, you
can use python-evtx to review the event logs of Windows 7 systems from a Mac or
Linux workstation. The structure definitions and parsing strategies were heavily
inspired by the work of Andreas Schuster and his Perl implementation
"Parse-Evtx".

%prep
%setup -q
%autopatch -p1

find Evtx -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%python_build

%install
%python_install
for c in %{commands}; do
  %python_clone -a %{buildroot}%{_bindir}/evtx_$c.py
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%{lua:for c in rpm.expand("%{commands}"):gmatch("%S+") do
  print(rpm.expand("%python_libalternatives_reset_alternative evtx_" .. c .. ".py"))
end}

%post
%{lua:for c in rpm.expand("%{commands}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative evtx_" .. c .. ".py"))
end}

%postun
%{lua:for c in rpm.expand("%{commands}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative evtx_" .. c .. ".py"))
end}

%files %{python_files}
%license LICENSE.TXT
%doc README.md
%{python_sitelib}/Evtx
%{python_sitelib}/python_evtx-%{version}*-info
%{lua:for c in rpm.expand("%{commands}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/evtx_" .. c .. ".py"))
end}

%changelog
