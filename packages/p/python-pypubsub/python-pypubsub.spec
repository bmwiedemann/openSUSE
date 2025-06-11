#
# spec file for package python-pypubsub
#
# Copyright (c) 2025 SUSE LLC
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


%global pypi_name pypubsub
Name:           python-%{pypi_name}
Version:        4.0.3
Release:        0
Summary:        Python Publish-Subscribe Package
License:        BSD-2-Clause
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Development/Python
URL:            https://github.com/schollii/pypubsub
Source:         https://github.com/schollii/%{pypi_name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests/suite
%pytest
popd

%files %{python_files}
%doc README.rst src/pubsub/RELEASE_NOTES.txt
%license src/pubsub/LICENSE_BSD_Simple.txt
%{python_sitelib}/pubsub
%{python_sitelib}/[Pp]ypubsub-%{version}*-info

%changelog
