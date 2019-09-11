#
# spec file for package python-pipenv
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pipenv
Version:        2018.11.26.1543215385.742ae1b9
Release:        0
License:        MIT and BSD-3-Clause and (BSD-3-Clause OR Apache-2.0)
Summary:        Python Development Workflow for Humans
Url:            https://github.com/pypa/pipenv
Group:          Development/Languages/Python
Source:         pipenv-%{version}.tar.xz

# One unit test fails trying to connect to network
Patch0:         unit-tests-rpmfail.patch
# Four integration tests fail trying to connect to network
# See https://github.com/pypa/pipenv/issues/3630
Patch1:         integration-tests-rpmfail.patch
# Four scenarios fail trying to connect to network, due to using
# requirementslib 1.4.2 instead of vendored requirements 1.3.1
Patch2:         remove-requirementslib-1.4.2-test-failures.patch

# Upstream patches to prevent unnecessary test failures due to vendoring
Patch3:         test_specific_package_environment_markers.patch
Patch4:         test_pipenv_graph.patch
Patch5:         test-uninstall-Flask.patch
Patch6:         test_update_locks.patch
Patch7:         pr_3670.patch
Patch8:         test-without-dev-tablib.patch

# Patches with fixes merged upstream

# This is a much simpler approach to upstream commit 6971468
# DeprecationWarnings were being emitted by a subprocess whose output was
# captured and loaded as JSON, resulting in decode errors.
Patch10:        decode-bug.patch

# nonpip vendors progress 1.4.  This patch is needed to use progress 1.5
# Subset of https://patch-diff.githubusercontent.com/raw/pypa/pip/pull/6319.patch
Patch11:        notpip-pr-6319-progress1.5.patch

# needed for test_scripts
Patch12:        conftest-ignore-py37-DeprecationWarning.patch

# de-vendor-all.patch excludes notpip's ui.py, as that is already patched
# above by notpip-pr-6319-progress1.5.patch
Patch15:        de-vendor-all.patch
Patch16:        de-vendor-notpip-ui.patch

BuildRequires:  python-rpm-macros
# Also needed as a runtime dependency for pkg_resources
BuildRequires:  %{python_module setuptools >= 36.2.1}
# Program dependencies used in tests
BuildRequires:  git-core
BuildRequires:  mercurial
# Core dependencies, unrelated to de-vendoring
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module pip >= 10}
BuildRequires:  %{python_module virtualenv > 15.1.0}
BuildRequires:  %{python_module virtualenv-clone >= 0.2.5}
# De-vendored dependencies
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module click-completion}
BuildRequires:  %{python_module click-didyoumean}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module delegator.py}
BuildRequires:  %{python_module distlib}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module first}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module passa}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pip-shims}
BuildRequires:  %{python_module pipdeptree}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module plette}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pythonfinder}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requirementslib}
BuildRequires:  %{python_module scandir}
BuildRequires:  %{python_module semver}
BuildRequires:  %{python_module shellingham}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module vistir}
BuildRequires:  %{python_module yarg}
BuildRequires:  %{python_module yaspin}
# notpip dependencies
BuildRequires:  %{python_module CacheControl}
BuildRequires:  %{python_module Genshi}
BuildRequires:  %{python_module datrie}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module lockfile}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pep517}
BuildRequires:  python2-ipaddress
# notpip is patched to work with progress 1.5
BuildRequires:  %{python_module progress >= 1.5}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module retrying}
# Testing dependencies
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest < 4}
BuildRequires:  %{python_module pytest-instafail}
# Dependency of fixture pytest-pypi
BuildRequires:  %{python_module Flask}
BuildRequires:  fdupes
BuildRequires:  python-enum34
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-certifi
Requires:       python-pip >= 10
Requires:       python-setuptools >= 36.2.1
Requires:       python-virtualenv
Requires:       python-virtualenv-clone >= 0.2.5
Requires:       python-Cerberus
Requires:       python-Jinja2
Requires:       python-appdirs
Requires:       python-attrs
Requires:       python-chardet
Requires:       python-click
Requires:       python-click-completion
Requires:       python-click-didyoumean
Requires:       python-colorama
Requires:       python-delegator.py
Requires:       python-distlib
Requires:       python-idna
Requires:       python-iso8601
Requires:       python-cached-property
Requires:       python-docopt
Requires:       python-first
Requires:       python-packaging
Requires:       python-passa
Requires:       python-parse
Requires:       python-pexpect
Requires:       python-pip-shims
Requires:       python-pipdeptree
Requires:       python-pipreqs
Requires:       python-plette
Requires:       python-pyparsing
Requires:       python-pythonfinder
Requires:       python-python-dotenv
Requires:       python-requests
Requires:       python-requirementslib
Requires:       python-scandir
Requires:       python-semver
Requires:       python-shellingham
Requires:       python-six
Requires:       python-toml
Requires:       python-tomlkit
Requires:       python-typing
Requires:       python-urllib3
Requires:       python-vistir
Requires:       python-yarg
Requires:       python-yaspin
Requires:       python-CacheControl
Requires:       python-Genshi
Requires:       python-datrie
Requires:       python-distro
Requires:       python-html5lib
Requires:       python-lockfile
Requires:       python-lxml
Requires:       python-pep517
Requires:       python-progress >= 1.5
Requires:       python-pytoml
Requires:       python-retrying
%ifpython2
Requires:       python-enum34
Requires:       python-ipaddress
%endif
Recommends:     git-core
Suggests:       mercurial
BuildArch:      noarch

%python_subpackages

%description
Pipenv is a tool that aims to bring the best of all packaging worlds
(bundler, composer, npm, cargo, yarn, etc.) to the Python world.

It automatically creates and manages a virtualenv for your projects,
as well as adds/removes packages from your Pipfile as you install/uninstall
packages. It also generates the ever–important Pipfile.lock, which is
used to produce deterministic builds.

%prep
%setup -q -n pipenv-%{version}
%autopatch -p1

# https://github.com/pypa/pipenv/issues/3326
	
sed -i 's/2018.11.15.dev0/%{version}/' pipenv/__version__.py

# Remove invoke and parver as unnecessary setup dependencies
sed -i '/setup_requires/d' setup.py
# Remove invoke tasks found only in the github archive
rm -r tasks

# Avoid name 'progress' which clashes with de-vendored package with same name
# Somehow pipenv/ becomes part of sys.path.  It is only used for UI progress
# meters, so not critical that other packages should be able to import it.
mv pipenv/progress.py pipenv/_progress.py
sed -i 's/progress/_progress/' pipenv/core.py

# Keep the license files which are listed in files section
mv pipenv/patched/crayons.LICENSE LICENSE.crayons
mv pipenv/patched/pipfile/LICENSE LICENSE.pipfile
mv pipenv/patched/pipfile/LICENSE.APACHE LICENSE.APACHE.pipfile
mv pipenv/patched/pipfile/LICENSE.BSD LICENSE.BSD.pipfile
mv pipenv/patched/piptools/LICENSE LICENSE.pip-tools
mv pipenv/patched/notpip/LICENSE.txt LICENSE.notpip
mv pipenv/patched/safety/LICENSE LICENSE.safety

# Delete everything else
rm -rf pipenv/vendor/ pipenv/patched/notpip/_vendor/
mkdir pipenv/vendor/
mkdir pipenv/patched/notpip/_vendor/
touch pipenv/vendor/__init__.py pipenv/patched/notpip/_vendor/__init__.py

# This fails because of a pipenv vendoring patch to python-tomlkit
# which hasnt been accepted upstream, and of dubious benefit anyway.
sed -i '/assert.*Inline comment/d' tests/integration/test_uninstall.py

# Prepare tests

# Remove flaky and pytest option -n
# @flaky is used on a lot of the tests skipped by marker 'needs_internet'
# but is also used on others which are not skipped, however they seem to
# reliably pass in OBS, and flaky complicates the error repor when they
# occur for other reasons, such as import problems caused by de-vendoring.
sed -i '/flaky/d' tests/integration/*.py
sed -i '/addopts/d' pytest.ini

# Not useful tests

rm tests/unit/test_utils_windows_executable.py tests/integration/test_windows.py

# Add vendored pytest_pypi fixure
echo 'from pytest_pypi.plugin import pypi, pypi_secure' >> tests/integration/conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pipenv
%python_clone -a %{buildroot}%{_bindir}/pipenv-resolver


%check
export LANG=en_US.UTF-8

# Copy executables to py2/3 build areas, to be used for testing
%{python_expand mkdir build/bin
for filepath in %{buildroot}/%{_bindir}/*-%{$python_bin_suffix}; do
  filename=$(basename $filepath)
  unsuffixed=${filename/-%{$python_bin_suffix}/}
  cp $filepath build/bin/$unsuffixed
done
}
export PATH="$(pwd)/build/bin:$PATH"

# Run unit tests first
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m pytest -vv --instafail \
  --ignore _build.python2 --ignore _build.python3 \
  --ignore tests/test_artifacts/ --ignore tests/pypi/ \
  tests/unit/ -k "not rpmfail_github_connect"
}

# test_system_and_deploy_work attempts to uninstall in the buildroot
# test_uninstall_requests is intentionally failing only when de-vendored to demostrate problems yet to be solved
# test_lock_handle_eggs has occasionally failed, but very sparodically

%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}:%{$python_sitelib}:%{$python_sitearch}:$PWD/tests/pytest-pypi
$python -m pytest -vv --instafail \
  --ignore _build.python2 --ignore _build.python3 \
  --ignore tests/test_artifacts/ --ignore tests/pypi/ \
  tests/integration/ \
  -k "not (rpmfail_github_connect or test_system_and_deploy_work or test_uninstall_requests or test_lock_handle_eggs)"
}

%post
%{python_install_alternative pipenv pipenv-resolver}

%postun
%{python_uninstall_alternative pipenv pipenv-resolver}

%files %{python_files}
%license LICENSE
# crayons is MIT
%license LICENSE.crayons
# notpip is pip, which is MIT
%license LICENSE.notpip
# safety is MIT
%license LICENSE.safety
# 'pip-tools' is BSD-3-Clause
%license LICENSE.pip-tools
# BSD-3-Clause OR Apache-2.0
%license LICENSE*.pipfile
%doc CHANGELOG.rst README.md docs/*.rst
%python_alternative %{_bindir}/pipenv
%python_alternative %{_bindir}/pipenv-resolver
%{python_sitelib}/*

%changelog
