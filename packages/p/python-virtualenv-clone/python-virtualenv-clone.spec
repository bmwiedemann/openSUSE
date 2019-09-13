#
# spec file for package python-virtualenv-clone
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
Name:           python-virtualenv-clone
Version:        0.5.3
Release:        0
Summary:        Script to clone virtualenvs
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/edwardgeorge/virtualenv-clone
Source:         https://files.pythonhosted.org/packages/source/v/virtualenv-clone/virtualenv-clone-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-virtualenv
BuildArch:      noarch
%python_subpackages

%description
virtualenv cloning script.

A script for cloning a non-relocatable virtualenv.

Virtualenv provides a way to make virtualenv's relocatable which could then be
copied as we wanted. However making a virtualenv relocatable this way breaks
the no-site-packages isolation of the virtualenv as well as other aspects that
come with relative paths and '%{_bindir}/env' shebangs that may be undesirable.

Also, the .pth and .egg-link rewriting doesn't seem to work as intended. This
attempts to overcome these issues and provide a way to easily clone an
existing virtualenv.

It performs the following:

- copies sys.argv[1] dir to sys.argv[2]
- updates the hardcoded VIRTUAL_ENV variable in the activate script to the
  new repo location. (--relocatable doesn't touch this)
- updates the shebangs of the various scripts in bin to the new python if
  they pointed to the old python. (version numbering is retained.)

    it can also change '%{_bindir}/env python' shebangs to be absolute too,
    though this functionality is not exposed at present.

- checks sys.path of the cloned virtualenv and if any of the paths are from
  the old environment it finds any .pth or .egg-link files within sys.path
  located in the new environment and makes sure any absolute paths to the
  old environment are updated to the new environment.

- finally it double checks sys.path again and will fail if there are still
  paths from the old environment present.

%prep
%setup -q -n virtualenv-clone-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# setup up update-alternatives
%python_clone -a %{buildroot}%{_bindir}/virtualenv-clone

%check
%python_exec setup.py test

%post
%python_install_alternative virtualenv-clone

%preun
%python_uninstall_alternative virtualenv-clone

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/virtualenv-clone
%{python_sitelib}/*

%changelog
