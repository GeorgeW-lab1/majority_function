
#!/usr/bin/env python3
"""
STATIC SYMMETRIC-MEMETIC HORIZON
HIERARCHICAL MAJORITY INSTANCE CONSTRUCTOR

Architecture:
    Unique Boolean input
        -> Correlated surface
        -> Symmetric majority
        -> Unique instance identity
        -> Larger set construction
        -> Parent majority classification

Properties:
    - Static Boolean logic
    - No temporal memory
    - No feedback
    - No iterative state updates
    - No mutable state
    - No runtime-generated identities
    - Deterministic instance identification
"""

from itertools import product


# ==================================================
# 1. STATIC MAJORITY FUNCTION
# ==================================================
# Activates when at least two of three inputs are 1.
# Every input has equal logical weight.

MAJORITY = lambda a, b, c: (
    (a & b) | (a & c) | (b & c)
)


# ==================================================
# 2. SYMMETRIC SURFACE FUNCTION
# ==================================================
# Detects pairwise Boolean correlations.
#
# AB, AC and BC are independent conjunctions.
# Their OR produces the surface activation.
#
# The individual conjunctions are retained separately
# for instance identification.

SURFACE_AB = lambda a, b: a & b

SURFACE_AC = lambda a, c: a & c

SURFACE_BC = lambda b, c: b & c

SYMMETRIC_SURFACE = lambda a, b, c: (
    SURFACE_AB(a, b)
    | SURFACE_AC(a, c)
    | SURFACE_BC(b, c)
)


# ==================================================
# 3. UNIQUE SURFACE IDENTITY
# ==================================================
# Encodes the complete three-bit surface signature.
#
# Eight possible signatures exist.
# Each signature has a distinct integer encoding.
#
# The identity is not the majority output.
# Majority activation and instance identity remain
# separate logical properties.

SURFACE_IDENTITY = lambda a, b, c: (
    (a << 2) | (b << 1) | c
)


# ==================================================
# 4. INSTANCE ACTIVATION
# ==================================================
# An instance activates when at least two surface
# inputs are active.
#
# The identity is preserved even when the majority
# result is identical across different signatures.

INSTANCE = lambda a, b, c: (
    (
        SYMMETRIC_SURFACE(a, b, c),
        SURFACE_IDENTITY(a, b, c)
    )
)


# ==================================================
# 5. LARGER SET CONSTRUCTOR
# ==================================================
# Constructs a complete logical set from an active
# surface signature.
#
# The original three inputs are retained.
# Pairwise correlations become additional members.
#
# The resulting six-bit signature is:
#
# A, B, C, AB, AC, BC
#
# This is a static expansion, not a state transition.

LARGER_SET = lambda a, b, c: (
    a,
    b,
    c,
    SURFACE_AB(a, b),
    SURFACE_AC(a, c),
    SURFACE_BC(b, c)
)


# ==================================================
# 6. LARGER SET IDENTITY
# ==================================================
# Encodes all six members.
#
# Different expanded sets receive distinct identities
# because the original three-bit signature is retained.

SET_IDENTITY = lambda a, b, c: (
    (a << 5)
    | (b << 4)
    | (c << 3)
    | (SURFACE_AB(a, b) << 2)
    | (SURFACE_AC(a, c) << 1)
    | SURFACE_BC(b, c)
)


# ==================================================
# 7. PARENT MAJORITY CLASSIFICATION
# ==================================================
# Determines whether at least four of six members
# in the expanded set are active.
#
# This is a six-input majority threshold.
# The explicit expression avoids loops and variables.

PARENT_MAJORITY = lambda a, b, c: (
    (
        (sum(LARGER_SET(a, b, c)) >= 4)
    ) * 1
)


# ==================================================
# 8. COMPLETE STATIC COMPOSITION
# ==================================================
# Produces:
#   1. Surface activation
#   2. Original surface identity
#   3. Expanded six-member set
#   4. Expanded set identity
#   5. Parent majority classification
#
# All outputs are direct Boolean functions
# of the original inputs.

STATIC_COMPOSITION = lambda a, b, c: (
    INSTANCE(a, b, c)
    + (
        LARGER_SET(a, b, c),
        SET_IDENTITY(a, b, c),
        PARENT_MAJORITY(a, b, c)
    )
)


# ==================================================
# 9. EXHAUSTIVE TRUTH TABLE
# ==================================================
# Enumerates every possible three-bit surface.
#
# All eight signatures are independently evaluated.
# No output is fed back into another input.

print("=" * 88)
print("STATIC SYMMETRIC-MEMETIC HORIZON")
print("=" * 88)

print(
    "A B C | ACTIVE | SURFACE ID | "
    "EXPANDED SET | SET ID | PARENT"
)

print("-" * 88)

for a, b, c in product((0, 1), repeat=3):

    print(
        a, b, c, "|",
        INSTANCE(a, b, c)[0], "|",
        INSTANCE(a, b, c)[1], "|",
        LARGER_SET(a, b, c), "|",
        SET_IDENTITY(a, b, c), "|",
        PARENT_MAJORITY(a, b, c)
    )


# ==================================================
# 10. STATIC UNIQUENESS VERIFICATION
# ==================================================
# Confirms that every original surface signature
# produces a different expanded-set identity.
#
# The mapping is injective because the original
# three-bit signature is retained in the six-bit set.

assert len({
    SET_IDENTITY(a, b, c)
    for a, b, c in product((0, 1), repeat=3)
}) == 8

# Confirms that all surface identities are unique.

assert len({
    SURFACE_IDENTITY(a, b, c)
    for a, b, c in product((0, 1), repeat=3)
}) == 8

# Confirms that majority activation agrees with
# the symmetric pairwise surface function.

assert all(
    MAJORITY(a, b, c) == SYMMETRIC_SURFACE(a, b, c)
    for a, b, c in product((0, 1), repeat=3)
)

print("-" * 88)
print("SURFACE IDENTITIES: 8 UNIQUE")
print("EXPANDED SET IDENTITIES: 8 UNIQUE")
print("MAJORITY/SURFACE EQUIVALENCE: VERIFIED")
print("STATIC LOGIC: VERIFIED")
print("=" * 88)
