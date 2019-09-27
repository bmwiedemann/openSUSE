#
# spec file for package python-fudge
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
Name:           python-fudge
Version:        1.1.1
Release:        0
Summary:        Module for replacing real objects with fakes (mocks, stubs, etc) while testing
License:        MIT
Group:          Development/Languages/Python
URL:            http://farmdev.com/projects/fudge/
Source:         https://files.pythonhosted.org/packages/source/f/fudge/fudge-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
BuildArch:      noarch
%python_subpackages

%description
Complete documentation is available at http://farmdev.com/projects/fudge/

Fudge is a Python module for using fake objects (mocks and stubs) to test real ones.

In readable Python code, you declare what methods are available on your fake and
how they should be called. Then you inject that into your application and start
testing. This declarative approach means you don't have to record and playback
actions and you don't have to inspect your fakes after running code. If the fake
object was used incorrectly then you'll see an informative exception message
with a traceback that points to the culprit.

%prep
%setup -q -n fudge-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir testdir
pushd testdir
%if 0%{?have_python2} && ! 0%{?skip_python2}
cp -r ../fudge/tests tests2
export PYTHONPATH=%{buildroot}%{python2_sitelib}
nosetests-%{python2_bin_suffix} -w tests2
%endif
%if 0%{?have_python3} && ! 0%{?skip_python3}
cp -r ../fudge/tests tests3
2to3 -w tests3
export PYTHONPATH=%{buildroot}%{python3_sitelib}
nosetests-%{python3_bin_suffix} -w tests3
%endif
popd

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
