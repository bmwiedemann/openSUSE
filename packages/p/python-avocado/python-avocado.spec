#
# spec file for package python-avocado
#
# Copyright (c) 2020 SUSE LLC
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


# No longer build for python2
%define skip_python2  1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         pkgname avocado
Name:           python-avocado
Version:        69.0
Release:        0
Summary:        Avocado Test Framework
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://avocado-framework.github.io/
Source:         https://github.com/avocado-framework/avocado/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module aexpect}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pystache}
BuildRequires:  %{python_module requests} >= 1.2.3
BuildRequires:  %{python_module resultsdb_api}
BuildRequires:  %{python_module setuptools} >= 18.0.0
BuildRequires:  %{python_module six} >= 1.11.0
BuildRequires:  %{python_module stevedore} >= 0.14
BuildRequires:  fdupes
BuildRequires:  kmod
BuildRequires:  libvirt-devel
BuildRequires:  procps
BuildRequires:  python-rpm-macros
Requires:       %{pkgname}-common
Requires:       gdb
Requires:       procps
Requires:       python-Fabric
Requires:       python-requests >= 1.2.3
Requires:       python-setuptools
Requires:       python-six >= 1.11.0
Requires:       python-stevedore >= 0.14
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
%ifpython2
Requires:       python2-pylzma
Requires:       python2-subprocess32 >= 3.2.6
%endif
%python_subpackages

%description
Avocado is a set of tools and libraries (what people call these days a
framework) to perform automated testing.

%package  -n    %{pkgname}-common
Summary:        Avocado Test Framework
Group:          Development/Languages/Python
Conflicts:      avocado < %{version}

%description   -n  %{pkgname}-common
Avocado is a set of tools and libraries (what people call these days a
framework) to perform automated testing.

This package contains common infrastructure files.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-output-html
Summary:        Avocado HTML report plugin
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-pystache

%description -n python2-%{pkgname}-plugins-output-html
This plugin adds the ability for Avocado to generate an HTML report in every
job result directory. It also gives the user the ability to write a report to
an arbitrary filesystem location.
%endif

%package -n python3-%{pkgname}-plugins-output-html
Summary:        Avocado HTML report plugin
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-pystache

%description -n python3-%{pkgname}-plugins-output-html
This plugin adds the ability for Avocado to generate an HTML report in every
job result directory. It also gives the user the ability to write a report to
an arbitrary filesystem location.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-runner-remote
Summary:        Avocado Runner for Remote Execution
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-Fabric

%description -n python2-%{pkgname}-plugins-runner-remote
This plugin allows Avocado to run jobs on a remote machine, by means of an SSH
connection. Avocado must have been previously installed on the remote machine.
%endif

%package -n python3-%{pkgname}-plugins-runner-remote
Summary:        Avocado Runner for Remote Execution
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-Fabric

%description -n python3-%{pkgname}-plugins-runner-remote
This plugin allows Avocado to run jobs on a remote machine, by means of an SSH
connection. Avocado must have been previously installed on the remote machine.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-runner-vm
Summary:        Avocado Runner for libvirt VM Execution
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-%{pkgname}-plugins-runner-remote = %{version}
Requires:       python2-libvirt-python

%description -n python2-%{pkgname}-plugins-runner-vm
This plugin allows Avocado to run jobs within a libvirt-based virtual machine,
by means of interaction with a libvirt daemon and an SSH connection to the VM
itself. Avocado must have been previously installed on the VM.
%endif

%package -n python3-%{pkgname}-plugins-runner-vm
Summary:        Avocado Runner for libvirt VM Execution
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-%{pkgname}-plugins-runner-remote = %{version}
Requires:       python3-libvirt-python

%description -n python3-%{pkgname}-plugins-runner-vm
This plugin allows Avocado to run jobs within a libvirt-based virtual machine,
by means of interaction with a libvirt daemon and an SSH connection to the VM
itself. Avocado must have been previously installed on the VM.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-runner-docker
Summary:        Avocado Runner for Execution on Docker Containers
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-%{pkgname}-plugins-runner-remote = %{version}
Requires:       python2-aexpect

%description -n python2-%{pkgname}-plugins-runner-docker
This plugin allows Avocado to run jobs within a Docker container, by
interacting with a Docker daemon and attaching to the container itself. Avocado
must have been previously installed in the container.
%endif

%package -n python3-%{pkgname}-plugins-runner-docker
Summary:        Avocado Runner for Execution on Docker Containers
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-%{pkgname}-plugins-runner-remote = %{version}
Requires:       python3-aexpect

%description -n python3-%{pkgname}-plugins-runner-docker
This plugin allows Avocado to run jobs within a Docker container, by
interacting with a Docker daemon and attaching to the container itself. Avocado
must have been previously installed in the container.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-resultsdb
Summary:        Avocado plugin to propagate job results to ResultsDB
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-resultsdb_api

%description -n python2-%{pkgname}-plugins-resultsdb
This plugin allows Avocado to send job results directly to a ResultsDB
server.
%endif

%package -n python3-%{pkgname}-plugins-resultsdb
Summary:        Avocado plugin to propagate job results to ResultsDB
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-resultsdb_api

%description -n python3-%{pkgname}-plugins-resultsdb
Allows Avocado to send job results directly to a ResultsDB
server.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-varianter-yaml-to-mux
Summary:        Avocado plugin to generate variants out of yaml files
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}
Requires:       python2-pyaml

%description -n python2-%{pkgname}-plugins-varianter-yaml-to-mux
This plugin can be used to produce multiple test variants with test parameters
defined in one or more YAML files.
%endif

%package -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
Summary:        Avocado plugin to generate variants out of yaml files
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}
Requires:       python3-pyaml

%description -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
This plugin can be used to produce multiple test variants with test parameters
defined in one or more YAML files.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-loader-yaml
Summary:        Avocado Plugin that loads tests from YAML files
Group:          Development/Languages/Python
Requires:       python2-%{pkgname}-plugins-varianter-yaml-to-mux = %{version}

%description -n python2-%{pkgname}-plugins-loader-yaml
This plugin can be used to produce a test suite from definitions in a YAML file,
similar to the one used in the yaml_to_mux varianter plugin.
%endif

%package -n python3-%{pkgname}-plugins-loader-yaml
Summary:        Avocado Plugin that loads tests from YAML files
Group:          Development/Languages/Python
Requires:       python3-%{pkgname}-plugins-varianter-yaml-to-mux = %{version}

%description -n python3-%{pkgname}-plugins-loader-yaml
This plugin can be used to produce a test suite from definitions in a YAML file,
similar to the one used in the yaml_to_mux varianter plugin.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-golang
Summary:        Avocado Plugin for Execution of golang tests
Group:          Development/Languages/Python
Requires:       go
Requires:       python2-%{pkgname} = %{version}

%description -n python2-%{pkgname}-plugins-golang
This plugin allows Avocado to list golang tests, and if golang is installed,
to also run them.
%endif

%package -n python3-%{pkgname}-plugins-golang
Summary:        Avocado Plugin for Execution of golang tests
Group:          Development/Languages/Python
Requires:       go
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-golang
This plugin allows Avocado to list golang tests, and if golang is installed,
to also run them.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-varianter-pict
Summary:        Varianter with combinatorial capabilities by PICT
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}

%description -n python2-%{pkgname}-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.
%endif

%package -n python3-%{pkgname}-plugins-varianter-pict
Summary:        Varianter with combinatorial capabilities by PICT
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.

%package -n python3-%{pkgname}-plugins-varianter-cit
Summary:        Varianter with Combinatorial Independent Testing capabilities
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-varianter-cit
A varianter plugin that generates variants using Combinatorial
Independent Testing (AKA Pair-Wise) algorithm developed in
collaboration with CVUT Prague.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-result-upload
Summary:        Avocado Plugin to propagate Job results to a remote host
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}

%description -n python2-%{pkgname}-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.
%endif

%package -n python3-%{pkgname}-plugins-result-upload
Summary:        Avocado Plugin to propagate Job results to a remote host
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.

%if 0%{?have_python2} && ! 0%{?skip_python2}
%package -n python2-%{pkgname}-plugins-glib
Summary:        Avocado Plugin for Execution of GLib Test Framework tests
Group:          Development/Languages/Python
Requires:       python2-%{pkgname} = %{version}

%description -n python2-%{pkgname}-plugins-glib
This optional plugin is intended to list and run tests written in the
GLib Test Framework.
%endif

%package -n python3-%{pkgname}-plugins-glib
Summary:        Avocado Plugin for Execution of GLib Test Framework tests
Group:          Development/Languages/Python
Requires:       python3-%{pkgname} = %{version}

%description -n python3-%{pkgname}-plugins-glib
This optional plugin is intended to list and run tests written in the
GLib Test Framework.

%package -n %{pkgname}-examples
Summary:        Avocado Test Framework Example Tests
Group:          Development/Tools/Other
Requires:       %{pkgname} = %{version}

%description -n %{pkgname}-examples
The set of example tests present in the upstream tree of the Avocado framework.
Some of them are used as functional tests of the framework, others serve as
examples of how to write tests on your own.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%python_build
make %{?_smp_mflags} man

pushd optional_plugins/html
%python_build
popd
pushd optional_plugins/runner_remote
%python_build
popd
pushd optional_plugins/runner_vm
%python_build
popd
pushd optional_plugins/runner_docker
%python_build
popd
pushd optional_plugins/resultsdb
%python_build
popd
pushd optional_plugins/varianter_yaml_to_mux
%python_build
popd
pushd optional_plugins/loader_yaml
%python_build
popd
pushd optional_plugins/golang
%python_build
popd
pushd optional_plugins/varianter_pict
%python_build
popd
pushd optional_plugins/result_upload
%python_build
popd
pushd optional_plugins/glib
%python_build
popd

%install
%python_install

pushd optional_plugins/html
%python_install
popd
pushd optional_plugins/runner_remote
%python_install
popd
pushd optional_plugins/runner_vm
%python_install
popd
pushd optional_plugins/runner_docker
%python_install
popd
pushd optional_plugins/resultsdb
%python_install
popd
pushd optional_plugins/varianter_yaml_to_mux
%python_install
popd
pushd optional_plugins/loader_yaml
%python_install
popd
pushd optional_plugins/golang
%python_install
popd
pushd optional_plugins/varianter_pict
%python_install
popd
pushd optional_plugins/result_upload
%python_install
popd
pushd optional_plugins/glib
%python_install
popd

%python_clone -a %{buildroot}%{_bindir}/avocado
%python_clone -a %{buildroot}%{_bindir}/avocado-rest-client

# Reduce duplicates
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install manpages
install -Dpm 0644 man/avocado.1 \
  %{buildroot}%{_mandir}/man1/avocado.1
install -Dpm 0644 man/avocado-rest-client.1 \
  %{buildroot}%{_mandir}/man1/avocado-rest-client.1

# Install etc
mv %{buildroot}%{python3_sitelib}/avocado%{_sysconfdir}/%{pkgname} \
  %{buildroot}%{_sysconfdir}/%{pkgname}

# Prepare common directories
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/avocado/data
install -d -m 0755 %{buildroot}%{_docdir}/avocado

# Install examples
cp -r examples/gdb-prerun-scripts %{buildroot}%{_docdir}/avocado
cp -r examples/plugins %{buildroot}%{_docdir}/avocado
cp -r examples/tests %{buildroot}%{_docdir}/avocado
cp -r examples/wrappers %{buildroot}%{_docdir}/avocado
cp -r examples/yaml_to_mux %{buildroot}%{_docdir}/avocado
cp -r examples/yaml_to_mux_loader %{buildroot}%{_docdir}/avocado
cp -r examples/varianter_pict %{buildroot}%{_docdir}/avocado

# Move libexecdir
mkdir -p %{buildroot}%{_libexecdir}/avocado
%if 0%{?have_python2} && ! 0%{?skip_python2}
%python2_only mv %{buildroot}%{python2_sitelib}/avocado/libexec/* %{buildroot}%{_libexecdir}/avocado
%else
%python3_only mv %{buildroot}%{python3_sitelib}/avocado/libexec/* %{buildroot}%{_libexecdir}/avocado
%endif

# Do not ship tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

# Do not ship libexecdir in wrong place
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{pkgname}/libexec

# Do not ship etc in wrong place
%python_expand rm -rf %{buildroot}%{$python_sitelib}/%{pkgname}%{_sysconfdir}

%post
%{python_install_alternative avocado avocado-rest-client}

%postun
%{python_uninstall_alternative avocado avocado-rest-client}

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/avocado
%python_alternative %{_bindir}/avocado-rest-client
%dir %{python_sitelib}/%{pkgname}
%pycache_only %{python_sitelib}/%{pkgname}/__pycache__
%{python_sitelib}/%{pkgname}/__init__.py*
%{python_sitelib}/%{pkgname}/__main__.py*
%{python_sitelib}/%{pkgname}/core
%{python_sitelib}/%{pkgname}/plugins
%{python_sitelib}/%{pkgname}/utils
%{python_sitelib}/%{pkgname}_framework-%{version}*

%files -n %{pkgname}-common
%license LICENSE
%dir %{_sysconfdir}/avocado
%dir %{_sysconfdir}/avocado/conf.d
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
%config(noreplace)%{_sysconfdir}/avocado/avocado.conf
%config(noreplace)%{_sysconfdir}/avocado/conf.d/README
%config(noreplace)%{_sysconfdir}/avocado/conf.d/gdb.conf
%config(noreplace)%{_sysconfdir}/avocado/conf.d/jobscripts.conf
%config(noreplace)%{_sysconfdir}/avocado/conf.d/resultsdb.conf
%config(noreplace)%{_sysconfdir}/avocado/conf.d/result_upload.conf
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/commands
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/files
%config(noreplace)%{_sysconfdir}/avocado/sysinfo/profilers
%config(noreplace)%{_sysconfdir}/avocado/scripts/job/pre.d/README
%config(noreplace)%{_sysconfdir}/avocado/scripts/job/post.d/README
%{_mandir}/man1/avocado-rest-client.1%{?ext_man}
%{_mandir}/man1/avocado.1%{?ext_man}

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-output-html
%{python2_sitelib}/avocado_result_html*
%{python2_sitelib}/avocado_framework_plugin_result_html*
%endif

%files -n python3-%{pkgname}-plugins-output-html
%{python3_sitelib}/avocado_result_html*
%{python3_sitelib}/avocado_framework_plugin_result_html*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-runner-remote
%{python2_sitelib}/avocado_runner_remote*
%{python2_sitelib}/avocado_framework_plugin_runner_remote*
%endif

%files -n python3-%{pkgname}-plugins-runner-remote
%{python3_sitelib}/avocado_runner_remote*
%{python3_sitelib}/avocado_framework_plugin_runner_remote*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-runner-vm
%{python2_sitelib}/avocado_runner_vm*
%{python2_sitelib}/avocado_framework_plugin_runner_vm*
%endif

%files -n python3-%{pkgname}-plugins-runner-vm
%{python3_sitelib}/avocado_runner_vm*
%{python3_sitelib}/avocado_framework_plugin_runner_vm*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-runner-docker
%{python2_sitelib}/avocado_runner_docker*
%{python2_sitelib}/avocado_framework_plugin_runner_docker*
%endif

%files -n python3-%{pkgname}-plugins-runner-docker
%{python3_sitelib}/avocado_runner_docker*
%{python3_sitelib}/avocado_framework_plugin_runner_docker*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-resultsdb
%{python2_sitelib}/avocado_resultsdb*
%{python2_sitelib}/avocado_framework_plugin_resultsdb*
%endif

%files -n python3-%{pkgname}-plugins-resultsdb
%{python3_sitelib}/avocado_resultsdb*
%{python3_sitelib}/avocado_framework_plugin_resultsdb*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-varianter-yaml-to-mux
%{python2_sitelib}/avocado_varianter_yaml_to_mux*
%{python2_sitelib}/avocado_framework_plugin_varianter_yaml_to_mux*
%endif

%files -n python3-%{pkgname}-plugins-varianter-yaml-to-mux
%{python3_sitelib}/avocado_varianter_yaml_to_mux*
%{python3_sitelib}/avocado_framework_plugin_varianter_yaml_to_mux*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-loader-yaml
%{python2_sitelib}/avocado_loader_yaml*
%{python2_sitelib}/avocado_framework_plugin_loader_yaml*
%endif

%files -n python3-%{pkgname}-plugins-loader-yaml
%{python3_sitelib}/avocado_loader_yaml*
%{python3_sitelib}/avocado_framework_plugin_loader_yaml*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-golang
%{python2_sitelib}/avocado_golang*
%{python2_sitelib}/avocado_framework_plugin_golang*
%endif

%files -n python3-%{pkgname}-plugins-golang
%{python3_sitelib}/avocado_golang*
%{python3_sitelib}/avocado_framework_plugin_golang*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-varianter-pict
%{python2_sitelib}/avocado_varianter_pict*
%{python2_sitelib}/avocado_framework_plugin_varianter_pict*
%endif

%files -n python3-%{pkgname}-plugins-varianter-pict
%{python3_sitelib}/avocado_varianter_pict*
%{python3_sitelib}/avocado_framework_plugin_varianter_pict*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-result-upload
%{python2_sitelib}/avocado_result_upload*
%{python2_sitelib}/avocado_framework_plugin_result_upload*
%endif

%files -n python3-%{pkgname}-plugins-result-upload
%{python3_sitelib}/avocado_result_upload*
%{python3_sitelib}/avocado_framework_plugin_result_upload*

%if 0%{?have_python2} && ! 0%{?skip_python2}
%files -n python2-%{pkgname}-plugins-glib
%{python2_sitelib}/avocado_glib*
%{python2_sitelib}/avocado_framework_plugin_glib*
%endif

%files -n python3-%{pkgname}-plugins-glib
%{python3_sitelib}/avocado_glib*
%{python3_sitelib}/avocado_framework_plugin_glib*

%files -n %{pkgname}-examples
%dir %{_docdir}/avocado
%{_docdir}/avocado/gdb-prerun-scripts
%{_docdir}/avocado/plugins
%{_docdir}/avocado/tests
%{_docdir}/avocado/wrappers
%{_docdir}/avocado/yaml_to_mux
%{_docdir}/avocado/yaml_to_mux_loader
%{_docdir}/avocado/varianter_pict

%changelog
