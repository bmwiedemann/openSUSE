#
# spec file for package python-temps
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-temps
Version:        0.3.0
Release:        0
Summary:        Context managers for creating and cleaning up temporary directories and files
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/todddeluca/temps
Source:         http://pypi.python.org/packages/source/t/temps/temps-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
temps is a python module containing context managers for creating and
cleaning up temporary files and directories.

* It has a context manager for creating a temp dir and another for
  temp files.
* The context manager cleans up the dir or file upon context exit,
  not upon file closure.
* No ambiguity about whether you can or cannot open a file twice.
* You can set the permissions of the temp file or dir to what you
  want.
* It is very clear what the implementation is:
  + directories are created and the path is returned.
  + files are not created, since you'll want to do that in a with
    open(filename) ... statement, and the path is returned.
  + directories and files are cleaned up by the context managers.
  + file and dir names are generated using the uuid module, which
    presumably will avoid race conditions.

%prep
%setup -q -n temps-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python setup.py -q test

%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%{python_sitelib}/*

%changelog
