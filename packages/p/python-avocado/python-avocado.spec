#
# spec file for package python-avocado
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# stevedore, aexpect anhd others are primary python3 only
%define pythons python3
%define         pkgname avocado
Name:           python-avocado
Version:        113.0
Release:        0
Summary:        Avocado Test Framework
License:        GPL-2.0-only
URL:            https://avocado-framework.github.io/
Source:         https://github.com/avocado-framework/avocado/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module aexpect}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pystache}
BuildRequires:  %{python_module requests >= 1.2.3}
BuildRequires:  %{python_module resultsdb_api}
BuildRequires:  %{python_module setuptools >= 18.0.0}
BuildRequires:  fdupes
BuildRequires:  kmod
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libvirt-admin)
BuildRequires:  pkgconfig(libvirt-lxc)
BuildRequires:  pkgconfig(libvirt-qemu)
Requires:       %{pkgname}-common
Requires:       gdb
Requires:       procps
Requires:       python-requests >= 1.2.3
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{pkgname} = %{version}
Obsoletes:      %{pkgname} < %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
BuildRequires:  %{python_module libvirt-python}
%else
BuildRequires:  python-libvirt-python
%endif
%python_subpackages

%description
Avocado is a set of tools and libraries (what people call these days a
framework) to perform automated testing.

%package  -n    %{pkgname}-common
Summary:        Avocado Test Framework
Conflicts:      avocado < %{version}

%description   -n  %{pkgname}-common
Avocado is a set of tools and libraries (what people call these days a
framework) to perform automated testing.

This package contains common infrastructure files.

%package -n python3-%{pkgname}-plugins-robot
Summary:        Avocado robot plugin
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-robotframework >= 4.1

%description -n python3-%{pkgname}-plugins-robot
This optional plugin enables Avocado to work with tests originally written
using the Robot Framework API.

%package -n python3-%{pkgname}-plugins-output-html
Summary:        Avocado HTML report plugin
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-pystache

%description -n python3-%{pkgname}-plugins-output-html
This plugin adds the ability for Avocado to generate an HTML report in every
job result directory. It also gives the user the ability to write a report to
an arbitrary filesystem location.

%package -n python3-%{pkgname}-plugins-resultsdb
Summary:        Avocado plugin to propagate job results to ResultsDB
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-resultsdb_api

%description -n python3-%{pkgname}-plugins-resultsdb
Allows Avocado to send job results directly to a ResultsDB
server.

%package -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
Summary:        Avocado plugin to generate variants out of yaml files
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-pyaml

%description -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
This plugin can be used to produce multiple test variants with test parameters
defined in one or more YAML files.

%package -n python3-%{pkgname}-plugins-golang
Summary:        Avocado Plugin for Execution of golang tests
Requires:       go
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-golang
This plugin allows Avocado to list golang tests, and if golang is installed,
to also run them.

%package -n python3-%{pkgname}-plugins-varianter-pict
Summary:        Varianter with combinatorial capabilities by PICT
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.

%package -n python3-%{pkgname}-plugins-varianter-cit
Summary:        Varianter with Combinatorial Independent Testing capabilities
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-varianter-cit
A varianter plugin that generates variants using Combinatorial
Independent Testing (AKA Pair-Wise) algorithm developed in
collaboration with CVUT Prague.

%package -n python3-%{pkgname}-plugins-result-upload
Summary:        Avocado Plugin to propagate Job results to a remote host
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.

%package -n python3-%{pkgname}-plugins-ansible
Summary:        Avocado plugin to run Ansible modules as tests
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-cffi

%description -n python3-%{pkgname}-plugins-ansible
This optional plugin enables Avocado to use Ansible modules as a source
of tests and as job dependencies.

%package -n python3-%{pkgname}-plugins-result-mail
Summary:        Avocado plugin to send job results by e-mail
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-result-mail
This optional plugin sends a notification e-mail with the Avocado job
results once a job finishes.

%package -n python3-%{pkgname}-plugins-spawner-remote
Summary:        Avocado spawner for running tests on a remote host
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-aexpect >= 1.6.2

%description -n python3-%{pkgname}-plugins-spawner-remote
This optional plugin adds a spawner that runs Avocado tests on a remote
host over SSH.

%package -n %{pkgname}-examples
Summary:        Avocado Test Framework Example Tests
Requires:       %{pkgname} = %{version}

%description -n %{pkgname}-examples
The set of example tests present in the upstream tree of the Avocado framework.
Some of them are used as functional tests of the framework, others serve as
examples of how to write tests on your own.

%prep
%setup -q -n %{pkgname}-%{version}

# fix shebang (also for the extension-less example test scripts)
pushd examples
find -type f -exec sed -i "1s|^#!\s*%{_bindir}/env python3|#!%{_bindir}/python3|" {} \;
popd

%build
%pyproject_wheel
%make_build man

pushd optional_plugins/html
%pyproject_wheel
popd
pushd optional_plugins/resultsdb
%pyproject_wheel
popd
pushd optional_plugins/robot
%pyproject_wheel
popd
pushd optional_plugins/varianter_yaml_to_mux
%pyproject_wheel
popd
pushd optional_plugins/golang
%pyproject_wheel
popd
pushd optional_plugins/varianter_pict
%pyproject_wheel
popd
pushd optional_plugins/varianter_cit
%pyproject_wheel
popd
pushd optional_plugins/result_upload
%pyproject_wheel
popd
pushd optional_plugins/ansible
%pyproject_wheel
popd
pushd optional_plugins/mail
%pyproject_wheel
popd
pushd optional_plugins/spawner_remote
%pyproject_wheel
popd

%install
%pyproject_install

pushd optional_plugins/robot
%pyproject_install
popd
pushd optional_plugins/varianter_cit
%pyproject_install
popd
pushd optional_plugins/html
%pyproject_install
popd
pushd optional_plugins/resultsdb
%pyproject_install
popd
pushd optional_plugins/varianter_yaml_to_mux
%pyproject_install
popd
pushd optional_plugins/golang
%pyproject_install
popd
pushd optional_plugins/varianter_pict
%pyproject_install
popd
pushd optional_plugins/result_upload
%pyproject_install
popd
pushd optional_plugins/ansible
%pyproject_install
popd
pushd optional_plugins/mail
%pyproject_install
popd
pushd optional_plugins/spawner_remote
%pyproject_install
popd

%python_clone -a %{buildroot}%{_bindir}/avocado
%python_clone -a %{buildroot}%{_bindir}/avocado-external-runner
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-ansible-module
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-asset
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-avocado-instrumented
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-dry-run
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-exec-test
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-golang
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-noop
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-package
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-pip
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-podman-image
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-python-unittest
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-robot
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-sysinfo
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-tap
%python_clone -a %{buildroot}%{_bindir}/avocado-runner-vmimage
%python_clone -a %{buildroot}%{_bindir}/avocado-software-manager

# force hash-based .pyc across core and all plugins
# (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}

# Reduce duplicates
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install manpages
install -Dpm 0644 man/avocado.1 \
  %{buildroot}%{_mandir}/man1/avocado.1

# Install etc
mv %{buildroot}%{python3_sitelib}/avocado%{_sysconfdir}/%{pkgname} \
  %{buildroot}%{_sysconfdir}/%{pkgname}

# Prepare common directories
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/avocado/data
install -d -m 0755 %{buildroot}%{_docdir}/avocado

# Install examples
cp -r examples/apis %{buildroot}%{_docdir}/avocado
cp -r examples/gdb-prerun-scripts %{buildroot}%{_docdir}/avocado
cp -r examples/hint-files %{buildroot}%{_docdir}/avocado
cp -r examples/jobs %{buildroot}%{_docdir}/avocado
cp -r examples/nrunner %{buildroot}%{_docdir}/avocado
cp -r examples/plugins %{buildroot}%{_docdir}/avocado
cp -r examples/testplans %{buildroot}%{_docdir}/avocado
cp -r examples/tests %{buildroot}%{_docdir}/avocado
cp -r examples/varianter_cit %{buildroot}%{_docdir}/avocado
cp -r examples/varianter_pict %{buildroot}%{_docdir}/avocado
cp -r examples/yaml_to_mux %{buildroot}%{_docdir}/avocado

# Move libexecdir
mkdir -p %{buildroot}%{_libexecdir}/avocado
%python3_only mv %{buildroot}%{python3_sitelib}/avocado/libexec/* %{buildroot}%{_libexecdir}/avocado

# Do not ship tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

# Do not ship libexecdir in wrong place
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{pkgname}/libexec

# Do not ship etc in wrong place
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{pkgname}%{_sysconfdir}

%post
%{python_install_alternative avocado avocado-external-runner avocado-runner-ansible-module avocado-runner-asset avocado-runner-avocado-instrumented avocado-runner-dry-run avocado-runner-exec-test avocado-runner-golang avocado-runner-noop avocado-runner-package avocado-runner-pip avocado-runner-podman-image avocado-runner-python-unittest avocado-runner-robot avocado-runner-sysinfo avocado-runner-tap avocado-runner-vmimage avocado-software-manager}

%postun
%{python_uninstall_alternative avocado avocado-external-runner avocado-runner-ansible-module avocado-runner-asset avocado-runner-avocado-instrumented avocado-runner-dry-run avocado-runner-exec-test avocado-runner-golang avocado-runner-noop avocado-runner-package avocado-runner-pip avocado-runner-podman-image avocado-runner-python-unittest avocado-runner-robot avocado-runner-sysinfo avocado-runner-tap avocado-runner-vmimage avocado-software-manager}

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/avocado
%python_alternative %{_bindir}/avocado-external-runner
%python_alternative %{_bindir}/avocado-runner-ansible-module
%python_alternative %{_bindir}/avocado-runner-asset
%python_alternative %{_bindir}/avocado-runner-avocado-instrumented
%python_alternative %{_bindir}/avocado-runner-dry-run
%python_alternative %{_bindir}/avocado-runner-exec-test
%python_alternative %{_bindir}/avocado-runner-golang
%python_alternative %{_bindir}/avocado-runner-noop
%python_alternative %{_bindir}/avocado-runner-package
%python_alternative %{_bindir}/avocado-runner-pip
%python_alternative %{_bindir}/avocado-runner-podman-image
%python_alternative %{_bindir}/avocado-runner-python-unittest
%python_alternative %{_bindir}/avocado-runner-robot
%python_alternative %{_bindir}/avocado-runner-sysinfo
%python_alternative %{_bindir}/avocado-runner-tap
%python_alternative %{_bindir}/avocado-runner-vmimage
%python_alternative %{_bindir}/avocado-software-manager

%dir %{python_sitelib}/%{pkgname}
%pycache_only %{python_sitelib}/%{pkgname}/__pycache__
%{python_sitelib}/%{pkgname}/__init__.py
%{python_sitelib}/%{pkgname}/__main__.py
%{python_sitelib}/%{pkgname}/core
%{python_sitelib}/%{pkgname}/plugins
%{python_sitelib}/%{pkgname}/schemas
%{python_sitelib}/%{pkgname}/utils
%{python_sitelib}/%{pkgname}_framework-%{version}.dist-info

%files -n %{pkgname}-common
%license LICENSE
%dir %{_sysconfdir}/avocado
%dir %{_sysconfdir}/avocado/sysinfo
%dir %{_sysconfdir}/avocado/scripts
%dir %{_sysconfdir}/avocado/scripts/job
%dir %{_sysconfdir}/avocado/scripts/job/pre.d
%dir %{_sysconfdir}/avocado/scripts/job/post.d
%dir %{_localstatedir}/lib/avocado
%dir %{_libexecdir}/avocado
%{_libexecdir}/avocado/avocado-bash-utils
%{_libexecdir}/avocado/avocado_debug
%{_libexecdir}/avocado/avocado_error
%{_libexecdir}/avocado/avocado_info
%{_libexecdir}/avocado/avocado_warn
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/commands
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/files
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/profilers
%config(noreplace)%{_sysconfdir}/avocado/scripts/job/pre.d/README
%config(noreplace)%{_sysconfdir}/avocado/scripts/job/post.d/README
%{_mandir}/man1/avocado.1%{?ext_man}

%files -n python3-%{pkgname}-plugins-robot
%{python3_sitelib}/avocado_robot
%{python3_sitelib}/avocado_framework_plugin_robot-%{version}.dist-info
%{_bindir}/avocado-runner-robot

%files -n python3-%{pkgname}-plugins-varianter-cit
%{python3_sitelib}/avocado_varianter_cit
%{python3_sitelib}/avocado_framework_plugin_varianter_cit-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-output-html
%{python3_sitelib}/avocado_result_html
%{python3_sitelib}/avocado_framework_plugin_result_html-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-resultsdb
%{python3_sitelib}/avocado_resultsdb
%{python3_sitelib}/avocado_framework_plugin_resultsdb-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
%{python3_sitelib}/avocado_varianter_yaml_to_mux
%{python3_sitelib}/avocado_framework_plugin_varianter_yaml_to_mux-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-golang
%{python3_sitelib}/avocado_golang
%{python3_sitelib}/avocado_framework_plugin_golang-%{version}.dist-info
%{_bindir}/avocado-runner-golang

%files -n python3-%{pkgname}-plugins-varianter-pict
%{python3_sitelib}/avocado_varianter_pict
%{python3_sitelib}/avocado_framework_plugin_varianter_pict-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-result-upload
%{python3_sitelib}/avocado_result_upload
%{python3_sitelib}/avocado_framework_plugin_result_upload-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-ansible
%{python3_sitelib}/avocado_ansible
%{python3_sitelib}/avocado_framework_plugin_ansible-%{version}.dist-info
%{_bindir}/avocado-runner-ansible-module

%files -n python3-%{pkgname}-plugins-result-mail
%{python3_sitelib}/avocado_result_mail
%{python3_sitelib}/avocado_framework_plugin_result_mail-%{version}.dist-info

%files -n python3-%{pkgname}-plugins-spawner-remote
%{python3_sitelib}/avocado_spawner_remote
%{python3_sitelib}/avocado_framework_plugin_spawner_remote-%{version}.dist-info

%files -n %{pkgname}-examples
%dir %{_docdir}/avocado
%{_docdir}/avocado/apis
%{_docdir}/avocado/gdb-prerun-scripts
%{_docdir}/avocado/hint-files
%{_docdir}/avocado/jobs
%{_docdir}/avocado/nrunner
%{_docdir}/avocado/plugins
%{_docdir}/avocado/testplans
%{_docdir}/avocado/tests
%{_docdir}/avocado/varianter_cit
%{_docdir}/avocado/varianter_pict
%{_docdir}/avocado/yaml_to_mux

%changelog
