
#!/usr/bin/env python3
"""
SSMHF
Static Symmetric-Memetic Horizon Majority Function

BOOLEAN KEYWORD SEARCH ENGINE WITH STATISTICS

Static Boolean computation:
    - Symmetric pairwise correlation
    - Two-of-three majority activation
    - Unique surface identities
    - Six-member set expansion
    - Parent majority classification

Search statistics:
    - Keyword match distribution
    - Activation rates
    - Unique instance counts
    - Surface distribution
    - Retrieval statistics
"""

import re
from collections import Counter


# ==================================================
# 1. DOCUMENT INDEX
# ==================================================

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
# 2. DETERMINISTIC TOKENIZATION
# ==================================================

TOKENIZE = lambda text: tuple(dict.fromkeys(
    re.findall(r"\b[a-z0-9]+\b", text.lower())
))


# ==================================================
# 3. QUERY ENCODING
# ==================================================

QUERY_TERMS = lambda query: TOKENIZE(query)[:3]


# ==================================================
# 4. BOOLEAN DOCUMENT MATCHING
# ==================================================

BOOLEAN_ENCODING = lambda keywords, document: tuple(
    int(keyword in TOKENIZE(document[1] + " " + document[2]))
    for keyword in keywords
)


# ==================================================
# 5. STATIC MAJORITY
# ==================================================

MAJORITY = lambda a, b, c: (
    (a & b) | (a & c) | (b & c)
)


# ==================================================
# 6. SYMMETRIC SURFACE
# ==================================================

SURFACE_AB = lambda a, b: a & b

SURFACE_AC = lambda a, c: a & c

SURFACE_BC = lambda b, c: b & c

SYMMETRIC_SURFACE = lambda a, b, c: (
    SURFACE_AB(a, b)
    | SURFACE_AC(a, c)
    | SURFACE_BC(b, c)
)


# ==================================================
# 7. SURFACE IDENTITY
# ==================================================

SURFACE_IDENTITY = lambda a, b, c: (
    (a << 2) | (b << 1) | c
)


# ==================================================
# 8. INSTANCE ACTIVATION
# ==================================================

INSTANCE = lambda a, b, c: (
    MAJORITY(a, b, c),
    SURFACE_IDENTITY(a, b, c)
)


# ==================================================
# 9. LARGER SET
# ==================================================

LARGER_SET = lambda a, b, c: (
    a,
    b,
    c,
    SURFACE_AB(a, b),
    SURFACE_AC(a, c),
    SURFACE_BC(b, c)
)


# ==================================================
# 10. SET IDENTITY
# ==================================================

SET_IDENTITY = lambda a, b, c: (
    (a << 5)
    | (b << 4)
    | (c << 3)
    | (SURFACE_AB(a, b) << 2)
    | (SURFACE_AC(a, c) << 1)
    | SURFACE_BC(b, c)
)


# ==================================================
# 11. PARENT MAJORITY
# ==================================================

PARENT_MAJORITY = lambda a, b, c: int(
    sum(LARGER_SET(a, b, c)) >= 4
)


# ==================================================
# 12. COMPLETE COMPOSITION
# ==================================================

STATIC_COMPOSITION = lambda a, b, c: (
    INSTANCE(a, b, c)
    + (
        LARGER_SET(a, b, c),
        SET_IDENTITY(a, b, c),
        PARENT_MAJORITY(a, b, c)
    )
)


# ==================================================
# 13. DOCUMENT EVALUATION
# ==================================================

EVALUATE = lambda keywords, document: (
    BOOLEAN_ENCODING(keywords, document)
)

ACTIVATED = lambda signature: MAJORITY(*signature)

MATCH_COUNT = lambda signature: sum(signature)


# ==================================================
# 14. PERCENTAGE
# ==================================================

PERCENT = lambda numerator, denominator: (
    100 * numerator / denominator
    if denominator else 0.0
)


# ==================================================
# 15. STATISTICS ENGINE
# ==================================================

def statistics(results, keywords):

    total = len(results)

    signatures = Counter(
        result["signature"]
        for result in results
    )

    match_distribution = Counter(
        result["matches"]
        for result in results
    )

    active = [
        result for result in results
        if result["active"]
    ]

    inactive = [
        result for result in results
        if not result["active"]
    ]

    parent_active = [
        result for result in results
        if result["parent"]
    ]

    unique_surface_ids = {
        result["surface_id"]
        for result in results
    }

    unique_set_ids = {
        result["set_id"]
        for result in results
    }

    print("\n" + "=" * 65)
    print("SSMHF SEARCH STATISTICS")
    print("=" * 65)

    print(f"Documents indexed:          {total}")
    print(f"Query keywords:             {len(keywords)}")
    print(f"Distinct query terms:       {len(set(keywords))}")

    print("\nKEYWORD MATCH DISTRIBUTION")

    for count in range(4):
        print(
            f"{count} of 3 matches:             "
            f"{match_distribution[count]} "
            f"({PERCENT(match_distribution[count], total):.2f}%)"
        )

    print("\nMAJORITY ACTIVATION")

    print(
        f"Activated documents:        {len(active)} "
        f"({PERCENT(len(active), total):.2f}%)"
    )

    print(
        f"Inactive documents:         {len(inactive)} "
        f"({PERCENT(len(inactive), total):.2f}%)"
    )

    print("\nINSTANCE STATISTICS")

    print(f"Unique surface signatures:  {len(unique_surface_ids)}")
    print(f"Unique expanded set IDs:    {len(unique_set_ids)}")

    print("\nPARENT CLASSIFICATION")

    print(
        f"Parent majority active:     {len(parent_active)} "
        f"({PERCENT(len(parent_active), total):.2f}%)"
    )

    print(
        f"Parent majority inactive:   {total - len(parent_active)}"
    )

    print("\nSURFACE DISTRIBUTION")

    for signature, count in sorted(signatures.items()):
        print(
            f"{signature}: {count} "
            f"({PERCENT(count, total):.2f}%)"
        )

    print("\nRETRIEVAL STATISTICS")

    print(f"Candidate results:           {len(active)}")
    print(f"Candidate rate:              {PERCENT(len(active), total):.2f}%")

    print(f"Documents with 3 matches:    {match_distribution[3]}")
    print(f"Documents with 2 matches:    {match_distribution[2]}")

    print("=" * 65)


# ==================================================
# 16. SEARCH ENGINE
# ==================================================

def search(query):

    keywords = QUERY_TERMS(query)

    if len(keywords) != 3:
        print("Please enter at least three distinct keywords.")
        return

    results = tuple(
        {
            "document": document,
            "signature": EVALUATE(keywords, document),
            "matches": MATCH_COUNT(EVALUATE(keywords, document)),
            "active": ACTIVATED(EVALUATE(keywords, document)),
            "surface_id": SURFACE_IDENTITY(
                *EVALUATE(keywords, document)
            ),
            "expanded": LARGER_SET(
                *EVALUATE(keywords, document)
            ),
            "set_id": SET_IDENTITY(
                *EVALUATE(keywords, document)
            ),
            "parent": PARENT_MAJORITY(
                *EVALUATE(keywords, document)
            )
        }
        for document in DOCUMENT_INDEX
    )

    print("\n" + "=" * 80)
    print("STATIC SYMMETRIC-MEMETIC HORIZON SEARCH")
    print("=" * 80)

    print("QUERY:", query)

    print("\nQUERY ENCODING")

    for index, keyword in enumerate(keywords):
        print(f"{'ABC'[index]} = {keyword}")

    print("\nDOCUMENT RESULTS")

    print(
        f"{'DOCUMENT':<10}"
        f"{'BITS':<12}"
        f"{'MATCH':<9}"
        f"{'ACTIVE':<9}"
        f"{'SURFACE':<10}"
        f"{'SET ID':<9}"
        f"{'PARENT':<8}"
    )

    print("-" * 80)

    for result in results:

        print(
            f"{result['document'][0]:<10}"
            f"{str(result['signature']):<12}"
            f"{result['matches']}/3{'':<5}"
            f"{str(result['active']):<9}"
            f"{result['surface_id']:<10}"
            f"{result['set_id']:<9}"
            f"{result['parent']:<8}"
        )

    print("\nACTIVATED CANDIDATES")

    for result in results:

        if result["active"]:

            print(
                f"\n{result['document'][0]}: "
                f"{result['document'][1]}"
            )

            print("Signature:", result["signature"])
            print("Surface ID:", result["surface_id"])
            print("Expanded set:", result["expanded"])
            print("Set identity:", result["set_id"])
            print("Parent majority:", result["parent"])

    statistics(results, keywords)


# ==================================================
# 17. STATIC LOGIC VERIFICATION
# ==================================================

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
        MAJORITY(a, b, c) ==
        SYMMETRIC_SURFACE(a, b, c)
        for a in (0, 1)
        for b in (0, 1)
        for c in (0, 1)
    )

    assert all(
        PARENT_MAJORITY(a, b, c) ==
        int(sum(LARGER_SET(a, b, c)) >= 4)
        for a in (0, 1)
        for b in (0, 1)
        for c in (0, 1)
    )

    print("Boolean verification: PASSED")
    print("Surface uniqueness: 8/8")
    print("Expanded identity uniqueness: 8/8")


# ==================================================
# 18. MAIN
# ==================================================

if __name__ == "__main__":

    verify()

    print("\nSSMHF KEYWORD SEARCH")
    print("Example: boolean majority correlation")

    search(input("\nSearch query: "))
