#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : onnx
Version  : 1.10.2
Release  : 44
URL      : https://files.pythonhosted.org/packages/16/6a/bdae938babb4bc23de7b599439f3d1f1179748385e4ced099f3b4cb646bd/onnx-1.10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/6a/bdae938babb4bc23de7b599439f3d1f1179748385e4ced099f3b4cb646bd/onnx-1.10.2.tar.gz
Summary  : Open Neural Network Exchange
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: onnx-bin = %{version}-%{release}
Requires: onnx-license = %{version}-%{release}
Requires: onnx-python = %{version}-%{release}
Requires: onnx-python3 = %{version}-%{release}
Requires: mypy
Requires: numpy
Requires: protobuf
Requires: six
Requires: typing_extensions
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : dos2unix
BuildRequires : mypy
BuildRequires : nbval
BuildRequires : numpy
BuildRequires : protobuf
BuildRequires : protobuf-dev
BuildRequires : pybind11-dev
BuildRequires : pytest
BuildRequires : pytest-runner
BuildRequires : python-tabulate
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : typing_extensions

%description
Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI
developers to choose the right tools as their project evolves. ONNX provides an
open source format for AI models, both deep learning and traditional ML. It
defines an extensible computation graph model, as well as definitions of
built-in operators and standard data types. Currently we focus on the
capabilities needed for inferencing (scoring).

%package bin
Summary: bin components for the onnx package.
Group: Binaries
Requires: onnx-license = %{version}-%{release}

%description bin
bin components for the onnx package.


%package license
Summary: license components for the onnx package.
Group: Default

%description license
license components for the onnx package.


%package python
Summary: python components for the onnx package.
Group: Default
Requires: onnx-python3 = %{version}-%{release}

%description python
python components for the onnx package.


%package python3
Summary: python3 components for the onnx package.
Group: Default
Requires: python3-core
Provides: pypi(onnx)
Requires: pypi(numpy)
Requires: pypi(protobuf)
Requires: pypi(six)
Requires: pypi(typing_extensions)

%description python3
python3 components for the onnx package.


%prep
%setup -q -n onnx-1.10.2
cd %{_builddir}/onnx-1.10.2

%build
## build_prepend content
find | xargs -n 1 dos2unix
# requires an additional archive to run these tests... avoid for now
#export ONNX_BUILD_TESTS=1
export CMAKE_ARGS="-DCMAKE_INSTALL_PREFIX=/usr"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636404052
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/onnx
cp %{_builddir}/onnx-1.10.2/LICENSE %{buildroot}/usr/share/package-licenses/onnx/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/onnx-1.10.2/third_party/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/onnx/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/onnx-1.10.2/third_party/pybind11/LICENSE %{buildroot}/usr/share/package-licenses/onnx/3dbd61e2b2c71dcc658c3da90bacf2e15958075a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/backend-test-tools
/usr/bin/check-model
/usr/bin/check-node

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/onnx/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/onnx/3dbd61e2b2c71dcc658c3da90bacf2e15958075a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
