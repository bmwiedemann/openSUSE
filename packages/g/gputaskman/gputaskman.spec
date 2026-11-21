#
# spec file for package gputaskman
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


# Single-flavour application: build against the primary python only, tracking it as it moves.
%define pythons %{primary_python}
Name:           gputaskman
Version:        0.4.3
Release:        0
Summary:        GPU task manager with per-process VRAM and LLM insights
License:        MIT
URL:            https://github.com/shanselman/gputaskman
Source:         https://github.com/shanselman/gputaskman/archive/refs/tags/v%{version}.tar.gz#/gputaskman-%{version}.tar.gz
# Upstream caps uv_build < 0.10.0, but Factory ships 0.13.x (upstream CI uses 0.13.6): keep only the floor.
# PATCH-FIX-OPENSUSE gputaskman-uv-build-cap.patch -- relax uv_build upper bound for Factory
Patch0:         gputaskman-uv-build-cap.patch
# Help-screen Markdown widget needs linkify at runtime (boo#1290249).
BuildRequires:  %{python_module linkify-it-py}
BuildRequires:  %{python_module nvidia-ml-py >= 13.615.71}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil >= 7.2.2}
BuildRequires:  %{python_module textual >= 8.2.8}
BuildRequires:  %{python_module uv-build >= 0.9.26}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-linkify-it-py
Requires:       %{primary_python}-nvidia-ml-py >= 13.615.71
Requires:       %{primary_python}-psutil >= 7.2.2
Requires:       %{primary_python}-textual >= 8.2.8
BuildArch:      noarch

%description
An htop for what's inside your GPU: per-process VRAM, engine load, and
LLM weights / KV-cache breakdown. Supports NVIDIA everywhere and
AMD/Intel on native Linux, with WSL and macOS support.

%prep
%autosetup -p1 -n gputaskman-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}

%check
%pyunittest discover -s tests -v

%files
%license LICENSE
%doc README.md
%{_bindir}/gputaskman
%{_bindir}/gtm
%{python_sitelib}/gputaskman
%{python_sitelib}/gputaskman-%{version}.dist-info

%changelog
