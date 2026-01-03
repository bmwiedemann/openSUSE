#
# spec file for package python-pyham_pe
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

%define mod_name pyham_pe
Name:           python-%{mod_name}
Version:        1.1.2
Release:        0
Summary:        Client implementation of the AGWPE protocol for packet radio
License:        MIT
URL:            https://pyham-pe.readthedocs.io/en/latest/
Source0:        https://github.com/mfncooper/pyham_pe/archive/refs/tags/v%{version}.tar.gz#/pyham_pe-%{version}.tar.gz
Source1:        https://www.on7lds.net/42/sites/default/files/AGWPEAPI.HTM
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
This package provides a client implementation of the AGWPE protocol, enabling
and simplifying the creation of applications using that protocol in order to
communicate with servers such as Direwolf or ldsped.

A lower level API provides access to the protocol at a level close to that of
individual AGWPE frames (not to be confused with AX.25 frames), enabling the
ultimate level of control over communication with the server.

A higher level API provides abstractions helpful in building more complex
applications, transparently taking care of some of the details, such as
connection management and monitoring.

The AGWPE protocol, and thus this package, has the advantage, over other
commonly used protocols such as KISS, that it can be easily used to create
connected-mode sessions. As such, it can be used to create many types of ham
radio software, from simple beaconing to full-fledged packet radio terminal
applications akin to Linpac. (See PyHam’s Paracon software for an example of
the latter.)

%prep
%autosetup -n pyham_pe-%{version}
cp %{SOURCE1} AGWPEAPI.HTM

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{mod_name} %{buildroot}%{$python_sitelib}/pe

%files %{python_files}
%license LICENSE
%doc README.md
%doc docs/index.rst
%doc docs/userguide.rst
%doc AGWPEAPI.HTM
%{python_sitelib}/%{mod_name}*
%{python_sitelib}/pe*

%changelog

