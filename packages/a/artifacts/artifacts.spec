#
# spec file for package artifacts
#
# Copyright (c) 2022 SUSE LLC
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


%define timestamp 20220429
Name:           artifacts
Version:        %{timestamp}
Release:        0
Summary:        Digital Forensics Artifact Repository
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/ForensicArtifacts/artifacts/wiki
Source0:        https://github.com/ForensicArtifacts/artifacts/releases/download/%{timestamp}/artifacts-%{timestamp}.tar.gz
Source1:        https://github.com/ForensicArtifacts/artifacts/releases/download/%{timestamp}/artifacts-%{timestamp}.tar.gz.asc
# Key 0xD9625E5D7AD0177E by Joachim Metz https://github.com/joachimmetz
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# security:forensics is now only supporting python 3.7 or newer
BuildRequires:  python3-setuptools > 3.7
BuildRequires:  python3-packaging > 3.7
BuildRequires:  %{python_module base >= 3.7}
BuildArch:      noarch

%description
A community-sourced, machine-readable knowledge base of forensic
artifacts that can be used both as an information source and within
other tools.

Using artifacts in tools just requires reading YAML. (The Python code
in the project is merely used to validate that the artifacts follow
the specification.)

For some background on the artifacts system and how its developers
expect it to be used, see the BlackHat presentation and Youtube video
from the GRR team.

%package validator
Summary:        Digital Forensics Artifact Repository Validator
Group:          Productivity/Security
Requires:       artifacts

%description validator
Python modules and program to validate the artifact data. It is
possible for programs to directly call these Python modules, but, by
design, said programs should work directly with the YAML files
themselves and not use these Python modules.

%prep
%setup -q -n artifacts-%{timestamp}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
# these are installed to the wrong dir by %{name}
rm %{buildroot}/usr/share/doc/%{name}/ACKNOWLEDGEMENTS
rm %{buildroot}/usr/share/doc/%{name}/AUTHORS
rm %{buildroot}/usr/share/doc/%{name}/LICENSE
rm %{buildroot}/usr/share/doc/%{name}/README

%files
%doc ACKNOWLEDGEMENTS AUTHORS README
%license LICENSE
%{_datadir}/artifacts

%files validator
%license LICENSE
%{python3_sitelib}/artifacts*
%{_bindir}/validator.py
%{_bindir}/stats.py

%changelog
