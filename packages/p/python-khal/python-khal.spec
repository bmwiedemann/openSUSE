#
# spec file for package python-khal
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python36 1
%define oldpython python
Name:           python-khal
Version:        0.10.5
Release:        0
Summary:        CLI calendar with CalDAV support
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://lostpackets.de/khal/
Source0:        https://files.pythonhosted.org/packages/source/k/khal/khal-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix tests with latest pytz version
# https://github.com/pimutils/khal/commit/f6c9b8a53a0f12222b2ee25c82229b0605b8785a
Patch0:         fix-pytz-tests.patch
BuildRequires:  %{python_module atomicwrites >= 0.1.7}
BuildRequires:  %{python_module click >= 3.2}
BuildRequires:  %{python_module click-log >= 0.2.0}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module icalendar >= 4.0.3}
# Test dependency added by Patch0
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tzlocal >= 1.0}
BuildRequires:  %{python_module urwid >= 1.3.0}
BuildRequires:  %{python_module vdirsyncer}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-atomicwrites
Requires:       python-click
Requires:       python-click-log
Requires:       python-configobj
Requires:       python-dateutil
Requires:       python-icalendar
Requires:       python-pytz
Requires:       python-pyxdg
Requires:       python-tzlocal
Requires:       python-urwid
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Khal is a CLI (console), CalDAV based calendar program, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%package -n python-khal-bash-completion
Summary:        Bash completion for khal
Requires:       bash-completion
Supplements:    (khal and bash-completion)
BuildArch:      noarch

%description -n python-khal-bash-completion
Bash shell completions for khal

%package -n python-khal-fish-completion
Summary:        Fish completion for khal
Requires:       fish
Supplements:    (khal and fish)
BuildArch:      noarch

%description -n python-khal-fish-completion
Fish shell completions for khal

%package -n python-khal-zsh-completion
Summary:        ZSH completion for khal
Group:          Productivity/File utilities
Supplements:    (khal and zsh)
BuildArch:      noarch

%description -n python-khal-zsh-completion
zsh shell completions for khal

%prep
%autosetup -p1 -n khal-%{version}

%build
%python_build

for shell in bash zsh fish; do
    PYTHONPATH="$PWD" _KHAL_COMPLETE=${shell}_source python3 ./bin/khal >khal.$shell
done

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/khal
%python_clone -a %{buildroot}%{_bindir}/ikhal
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -Dm644 khal.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/khal
install -Dm644 khal.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_khal
install -Dm644 khal.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/khal.fish

%check
# Requires /dev/tty working
# https://github.com/pimutils/khal/issues/683
donttest="test_import_from_stdin"
# Broken tests with latest pytz versions
donttest+=" or test_bogota or test_event_no_dst"
%pytest -k "not (${donttest})"

%post
%python_install_alternative khal
%python_install_alternative ikhal

%postun
%python_uninstall_alternative khal
%python_uninstall_alternative ikhal

%files %{python_files}
%license COPYING
%doc AUTHORS.txt CONTRIBUTING.rst README.rst khal.conf.sample
%{python_sitelib}/khal
%{python_sitelib}/khal-%{version}*-info
%python_alternative %{_bindir}/khal
%python_alternative %{_bindir}/ikhal

%files -n python-khal-bash-completion
%{_datadir}/bash-completion/completions/khal

%files -n python-khal-fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/khal.fish

%files -n python-khal-zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_khal

%changelog
