# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%if 0%{?fedora}
  %bcond_without unit_tests
%endif
%if 0%{?rhel}
  %bcond_with unit_tests
%endif
%if 0%{?suse_version}
  %if 0%{?suse_version} > 1320
    #openSUSE Factory
    %bcond_without unit_tests
  %else
    %if 0%{?suse_version} == 1315
      #SLE12 or openSUSE LEAP
      %if 0%{?sle_version} == 120200
        # openSUSE LEAP 42.2
        %bcond_with unit_tests
      %else
        #SLE12 does not have deps
        %bcond_with unit_tests
      %endif
    %else
      # Older SUSE release
      %bcond_with unit_tests    
    %endif
  %endif
%endif

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-ceph-cfg
Version:        0.2.3+git.1478902462.f898834
Release:        0
Summary:        Python library to Admin and deploy Ceph
License:        Apache-2.0
Group:          System/Filesystems
Url:            https://github.com/ceph/ceph-deploy
Source0:        %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArchitectures: noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?suse_version}
BuildRequires:  python-base
%endif
%if 0%{with unit_tests}
BuildRequires:  python-virtualenv
BuildRequires:  python-tox
BuildRequires:  python-pip
BuildRequires:  python-flake8
BuildRequires:  python-pip
BuildRequires:  python-pyflakes
BuildRequires:  python-mock
BuildRequires:  python-coverage
%if 0%{?suse_version}
BuildRequires:  python-pytest >= 2.1.3
%endif
%if (0%{?fedora} > 12 || 0%{?rhel} > 5)
BuildRequires:  pytest
%endif
%endif
Requires:  parted
Requires:  gptfdisk
Requires:  util-linux

%description
An easy to use library to make tools to admin and deploy ceph storage clusters.
Ceph is a distributed network storage service. This library is used by salt-ceph
to configure ceph.

%prep
%setup -q

# Pre-populate the directory so that this step is avoided.
%setup -q -T -D -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
%if 0%{with unit_tests}
# Call the unit tests directly as OBS blocks internet connection for builds
# python setup.py test
py.test
flake8 --select=F,E9 ceph_cfg
%endif

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*

%changelog
