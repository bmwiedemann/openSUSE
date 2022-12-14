#
# spec file for package imgui
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


Name:           imgui
Version:        1.89.1
Release:        0
Summary:        Immediate Mode Graphical User interface for C++ with minimal dependencies
License:        MIT
Group:          System/Libraries
URL:            https://www.dearimgui.org
Source:         https://github.com/ocornut/imgui/archive/v%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  make

%description
ImGui is a bloat-free graphical user interface library for C++. It outputs
optimized vertex buffers that you can render anytime in your 3D-pipeline
enabled application. It is fast, portable, renderer agnostic and self-contained
(no external dependencies).

ImGui is designed to enable fast iteration and empower programmers to create
content creation tools and visualization/ debug tools (as opposed to UI for the
average end-user). It favors simplicity and productivity toward this goal, and
thus lacks certain features normally found in more high-level libraries.

ImGui is particularly suited to integration in realtime 3D applications,
fullscreen applications, embedded applications, games, or any applications on
consoles platforms where operating system features are non-standard.

%package devel
Summary:        Development files for ImGui
Group:          Development/Libraries/C and C++

%description devel
ImGui is self-contained within a few files that you can easily copy and compile
into your application/engine.

No specific build process is required. You can add the .cpp files to your
project or #include them from an existing file.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_includedir}/imgui
cp *.h %{buildroot}%{_includedir}/imgui

%files devel
%{_includedir}/imgui

%changelog
