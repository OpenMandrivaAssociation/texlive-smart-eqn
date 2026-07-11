%global tl_name smart-eqn
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Automatic math symbol styling for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/smart-eqn
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In LaTeX typesetting, one usually needs to use different variants of a
math symbol to clarify the meanings. For example, in linear algebra
literature, it is common to use boldfaced symbols to represent vectors,
and normal symbols to represent scalars. However, applying these
variants by typing \mathbf, \mathrm commands manually can be daunting.
This package aims to provide an automatic and customizable approach for
math symbol styling which eliminates the need to enter style commands
repeatedly.

