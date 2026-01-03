#
# spec file for package python-pyham_ax25
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define mod_name pyham_ax25
Name:           python-%{mod_name}
Version:        1.0.3
Release:        0
Summary:        Modules for working with AX.25 packets in an amateur packet radio env
License:        MIT
URL:            https://pyham-ax25.readthedocs.io/en/latest/
Source0:        https://github.com/mfncooper/pyham_ax25/archive/refs/tags/v%{version}.tar.gz#/pyham_ax25-%{version}.tar.gz
Source1:        https://web.tapr.org/tech_docs/AX25/AX25.2.2.pdf
Source2:        https://packet-radio.net/wp-content/uploads/2017/04/netrom1.pdf
BuildRequires:  fdupes
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module flit-core}
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
The ax25 and ax25.netrom modules provide structure definitions together with
methods to pack and unpack native AX.25 frames and NET/ROM routing table
updates. These modules work on all platforms, and can be used together with
the transport mechanism(s) of your choice.

The ax25.ports and ax25.socket modules provide facilities for working with
the Linux native AX.25 stack. Unlike other Python AX.25 packages, this includes
the creation and use of connected-mode sessions, and thus it is not limited to
unproto (UI frame) usage.

%prep
%autosetup -n pyham_ax25-%{version}
cp %{SOURCE1} AX25.2.2.pdf
cp %{SOURCE2} netrom1.pdf

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{mod_name} %{buildroot}%{$python_sitelib}/ax25

%check
export PYTHONPATH='.'
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%doc docs/examples.rst
%doc docs/index.rst
%doc docs/userguide.rst
%doc AX25.2.2.pdf
%doc netrom1.pdf
%{python_sitelib}/%{mod_name}*
%{python_sitelib}/ax25*

%changelog

