
#!/usr/bin/env python3
"""
SSMHMF
Static Symmetric-Memetic Horizon Majority Function

BOOLEAN KEYWORD SEARCH ENGINE

Features:
    - Keyword tokenisation
    - Boolean document indexing
    - Symmetric pairwise correlation
    - Two-of-three majority activation
    - Unique surface identification
    - Six-member set expansion
    - Parent majority classification
    - Candidate document retrieval
    - Static deterministic evaluation

No temporal memory, feedback, learning, or mutable
logical state is used by the Boolean engine.
"""

import re


# ==================================================
# 1. STATIC DOCUMENT INDEX
# ==================================================
# Each document has:
#   (document ID, title, content)
#
# Add documents to this tuple to expand the index.
# The index remains fixed during each search.

DOCUMENT_INDEX = (
    (
        "DOC001",
        "Symmetric Boolean Logic",
        "majority function boolean logic symmetric "
        "correlation surface pairwise conjunction"
    ),
    (
        "DOC002",
        "Hierarchical Set Construction",
        "hierarchical boolean sets unique identity "
        "surface activation larger set construction"
    ),
    (
        "DOC003",
        "Keyword Search Architecture",
        "keyword search document retrieval query "
        "matching boolean indexing"
    ),
    (
        "DOC004",
        "Memetic Horizon",
        "memetic horizon majority correlation "
        "surface targeting logical instance"
    ),
    (
        "DOC005",
        "Static Combinational Logic",
        "static boolean combinational logic "
        "deterministic majority gates"
    ),
    (
        "DOC006",
        "Correlation and Classification",
        "correlation classification keyword "
        "matching pairwise majority function"
    ),
    (
        "DOC007",
        "Instance Identification",
        "unique instance identity boolean signature "
        "larger set identification"
    ),
    (
        "DOC008",
        "Document Retrieval",
        "document search retrieval indexed "
        "keywords query classification"
    ),
)


# ==================================================
# 2. TEXT TOKENISATION
# ==================================================
# Converts text into a set of lowercase keywords.
# Punctuation is excluded.
# Repeated keywords do not create extra matches.

TOKENIZE = lambda text: frozenset(
    re.findall(r"\b[a-z0-9]+\b", text.lower())
)


# ==================================================
# 3. QUERY ENCODING
# ==================================================
# Three distinct query keywords become three Boolean
# surface inputs.
#
# Keyword order defines the A, B, C positions.
# Each document is independently evaluated against
# the same query signature.

QUERY_TERMS = lambda query: tuple(
    dict.fromkeys(TOKENIZE(query))
)[:3]


# ==================================================
# 4. BOOLEAN DOCUMENT MATCHING
# ==================================================
# Each keyword becomes:
#   1 = present in document
#   0 = absent from document
#
# This produces the three-bit search surface.

BOOLEAN_ENCODING = lambda keywords, document: tuple(
    int(keyword in TOKENIZE(document))
    for keyword in keywords
)


# ==================================================
# 5. STATIC MAJORITY FUNCTION
# ==================================================
# Two-of-three Boolean activation.
# All inputs have equal logical weight.

MAJORITY = lambda a, b, c: (
    (a & b) | (a & c) | (b & c)
)


# ==================================================
# 6. SYMMETRIC CORRELATION SURFACE
# ==================================================
# Three independent pairwise conjunctions.

SURFACE_AB = lambda a, b: a & b

SURFACE_AC = lambda a, c: a & c

SURFACE_BC = lambda b, c: b & c

SYMMETRIC_SURFACE = lambda a, b, c: (
    SURFACE_AB(a, b)
    | SURFACE_AC(a, c)
    | SURFACE_BC(b, c)
)


# ==================================================
# 7. UNIQUE SURFACE IDENTITY
# ==================================================
# Preserves the complete three-bit signature.
#
# Different surface configurations cannot share
# the same identity.

SURFACE_IDENTITY = lambda a, b, c: (
    (a << 2) | (b << 1) | c
)


# ==================================================
# 8. INSTANCE ACTIVATION
# ==================================================
# Separates activation from identity.
#
# The majority output determines activation.
# The signature determines instance identity.

INSTANCE = lambda a, b, c: (
    SYMMETRIC_SURFACE(a, b, c),
    SURFACE_IDENTITY(a, b, c)
)


# ==================================================
# 9. LARGER SET CONSTRUCTOR
# ==================================================
# Expands the original surface into six members:
#
# A, B, C, AB, AC, BC
#
# Pairwise correlations become additional
# logical members of the larger set.

LARGER_SET = lambda a, b, c: (
    a,
    b,
    c,
    SURFACE_AB(a, b),
    SURFACE_AC(a, c),
    SURFACE_BC(b, c)
)


# ==================================================
# 10. UNIQUE SET IDENTITY
# ==================================================
# Encodes all six Boolean members.
# The original signature remains recoverable.
#
# Eight original signatures produce eight unique
# expanded-set identities.

SET_IDENTITY = lambda a, b, c: (
    (a << 5)
    | (b << 4)
    | (c << 3)
    | (SURFACE_AB(a, b) << 2)
    | (SURFACE_AC(a, c) << 1)
    | SURFACE_BC(b, c)
)


# ==================================================
# 11. PARENT MAJORITY CLASSIFICATION
# ==================================================
# Four-of-six threshold over the expanded set.
#
# This is an additional classification output.
# It does not replace the initial activation.

PARENT_MAJORITY = lambda a, b, c: int(
    sum(LARGER_SET(a, b, c)) >= 4
)


# ==================================================
# 12. COMPLETE STATIC SEARCH EVALUATION
# ==================================================
# Produces all logical outputs for one document.

STATIC_COMPOSITION = lambda a, b, c: (
    INSTANCE(a, b, c)
    + (
        LARGER_SET(a, b, c),
        SET_IDENTITY(a, b, c),
        PARENT_MAJORITY(a, b, c)
    )
)


# ==================================================
# 13. DOCUMENT SEARCH
# ==================================================
# Evaluates every indexed document independently.
#
# Only documents with an activated majority surface
# become retrieval candidates.
#
# The parent classification is reported separately.

SEARCH_DOCUMENT = lambda keywords, document: (
    BOOLEAN_ENCODING(
        keywords,
        document[1] + " " + document[2]
    )
)


# ==================================================
# 14. SEARCH REPORT
# ==================================================

def search(query):

    if len(QUERY_TERMS(query)) != 3:
        print("\nEnter exactly three distinct keywords.")
        return

    print("\n" + "=" * 75)
    print("SSMHF STATIC BOOLEAN KEYWORD SEARCH")
    print("=" * 75)

    print("QUERY:", query)

    print("\nKEYWORD ENCODING")

    print("A:", QUERY_TERMS(query)[0])
    print("B:", QUERY_TERMS(query)[1])
    print("C:", QUERY_TERMS(query)[2])

    print("\n" + "-" * 75)
    print("DOCUMENT EVALUATION")
    print("-" * 75)

    print(
        "DOCUMENT | SURFACE | ACTIVE | "
        "SURFACE ID | SET ID | PARENT"
    )

    print("-" * 75)

    for document in DOCUMENT_INDEX:

        print("\nDOCUMENT:", document[0])
        print("TITLE:", document[1])

        print("MATCH:", document[2])

        print(
            "BOOLEAN:",
            SEARCH_DOCUMENT(QUERY_TERMS(query), document)
        )

        print(
            "RESULT:",
            STATIC_COMPOSITION(
                *SEARCH_DOCUMENT(QUERY_TERMS(query), document)
            )
        )

    print("\n" + "=" * 75)
    print("RETRIEVAL CANDIDATES")
    print("=" * 75)

    for document in DOCUMENT_INDEX:

        print(
            document[0],
            document[1],
            "SURFACE:",
            SEARCH_DOCUMENT(QUERY_TERMS(query), document),
            "ACTIVATED:",
            INSTANCE(
                *SEARCH_DOCUMENT(QUERY_TERMS(query), document)
            )[0]
        ) if MAJORITY(
            *SEARCH_DOCUMENT(QUERY_TERMS(query), document)
        ) else None

    print("\nSEARCH COMPLETE.")
    print("=" * 75)


# ==================================================
# 15. STATIC LOGIC VERIFICATION
# ==================================================
# Verify all eight possible surface configurations.
#
# No search result is used to modify another result.

def verify():

    assert len({
        SURFACE_IDENTITY(a, b, c)
        for a in (0, 1)
        for b in (0, 1)
        for c in (0, 1)
    }) == 8

    assert len({
        SET_IDENTITY(a, b, c)
        for a in (0, 1)
        for b in (0, 1)
        for c in (0, 1)
    }) == 8

    assert all(
        MAJORITY(a, b, c)
        == SYMMETRIC_SURFACE(a, b, c)
        for a in (0, 1)
        for b in (0, 1)
        for c in (0, 1)
    )

    assert all(
        SURFACE_IDENTITY(*(
            (i >> 2) & 1,
            (i >> 1) & 1,
            i & 1
        )) == i
        for i in range(8)
    )

    print("STATIC BOOLEAN VERIFICATION: PASSED")


# ==================================================
# 16. COMMAND-LINE INTERFACE
# ==================================================

if __name__ == "__main__":

    verify()

    print("\nSSMHF KEYWORD RETRIEVAL")
    print("Enter three distinct keywords.")
    print("Example: boolean majority correlation")

    search(input("\nSearch query: "))
