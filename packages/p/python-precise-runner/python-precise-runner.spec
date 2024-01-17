#
# spec file for package python-precise-runner
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-precise-runner
Version:        0.3.1
Release:        0
Summary:        Wrapper to use Mycroft Precise Wake Word Listener
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/MycroftAI/mycroft-precise
Source:         https://files.pythonhosted.org/packages/source/p/precise-runner/precise-runner-%{version}.tar.gz
# https://github.com/MycroftAI/mycroft-precise/issues/74
Source99:       https://raw.githubusercontent.com/MycroftAI/mycroft-precise/dev/LICENSE
BuildRequires:  %{python_module PyAudio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyAudio
BuildArch:      noarch
%python_subpackages

%description
Wrapper to use the Mycroft Precise Wake Word Listener

%prep
%setup -q -n precise-runner-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
