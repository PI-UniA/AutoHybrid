using AutoHybrid
using Documenter

DocMeta.setdocmeta!(AutoHybrid, :DocTestSetup, :(using AutoHybrid); recursive=true)

makedocs(;
    modules=[AutoHybrid],
    authors="Patrick Zimbrod <patrick.zimbrod@gmail.com> and contributors",
    repo="https://github.com/pzimbrod/AutoHybrid.jl/blob/{commit}{path}#{line}",
    sitename="AutoHybrid.jl",
    format=Documenter.HTML(;
        prettyurls=get(ENV, "CI", "false") == "true",
        canonical="https://pzimbrod.github.io/AutoHybrid.jl",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/pzimbrod/AutoHybrid.jl",
    devbranch="main",
)
