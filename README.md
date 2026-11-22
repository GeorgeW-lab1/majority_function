# Static Symmetric-Memetic Horizon Majority Function (SSMHMF)

## Overview

The Static Symmetric-Memetic Horizon Majority Function is a deterministic Boolean architecture that combines symmetric surface correlation, majority activation, unique instance identification, and hierarchical set construction.

The system treats a correlated Boolean surface as the activation boundary for constructing a larger logical instance.

Unlike sequential or adaptive architectures, all operations are evaluated directly from the original Boolean inputs. No temporal memory, feedback, iterative updates, or mutable state are required.

## Core Architecture

```text
       UNIQUE BOOLEAN INPUT
              A, B, C
                 |
                 v
       SYMMETRIC SURFACE
          AB, AC, BC
                 |
                 v
        MAJORITY ACTIVATION
                 |
                 v
       UNIQUE SURFACE IDENTITY
                 |
                 v
        LARGER SET CONSTRUCTOR
        A, B, C, AB, AC, BC
                 |
                 v
         UNIQUE SET IDENTITY
                 |
                 v
       PARENT MAJORITY CLASSIFIER
```

## 1. Symmetric Majority Function

The majority function activates when at least two of three Boolean inputs are active.

\[
M(A,B,C)=(A\land B)\lor(A\land C)\lor(B\land C)
\]

All three inputs have equal logical weight.

## 2. Symmetric Surface Correlation

The surface consists of three pairwise conjunctions:

\[
S(A,B,C)=\{AB,AC,BC\}
\]

The surface activates when any pair is simultaneously active.

This produces four active signatures:

- `110`
- `101`
- `011`
- `111`

Each signature represents a distinct Boolean configuration.

## 3. Unique Surface Identification

The original three-bit surface signature is preserved as an integer identity.

\[
I_s=4A+2B+C
\]

This provides eight possible unique identities.

Importantly, the majority output is not used as the identity because multiple surface configurations produce the same majority result.

## 4. Larger Set Construction

An active surface can be expanded into a six-member Boolean set:

\[
\mathcal S(A,B,C)=
\{A,B,C,AB,AC,BC\}
\]

The expanded set contains:

- Three original Boolean inputs.
- Three pairwise correlation outputs.

This creates a larger logical representation without requiring temporal propagation.

## 5. Expanded Set Identity

The expanded set receives a unique six-bit encoding:

\[
I_{\mathcal S}=
32A+16B+8C+4AB+2AC+BC
\]

Because the original three inputs are retained, the mapping is injective.

Different original surface signatures cannot produce the same expanded-set identity.

## 6. Parent Majority Classification

The expanded set can be classified using a four-of-six threshold:

\[
P(\mathcal S)=
\begin{cases}
1 & \sum \mathcal S\geq4\\
0 & \sum \mathcal S<4
\end{cases}
\]

This provides a second-level majority classification.

## 7. Logical Properties

| Property | Implementation |
|---|---|
| Logic type | Static Boolean |
| Surface | Three pairwise conjunctions |
| Activation | Two-of-three majority |
| Surface identities | 8 |
| Expanded set size | 6 members |
| Expanded identities | 8 |
| Set classification | Four-of-six |
| Feedback | None |
| Temporal memory | None |
| Iterative updates | None |
| Determinism | Guaranteed |

## 8. Implementation

The complete implementation is contained in:

`smhmf.py`

Run:

```bash
python smhmf.py
```

The program exhaustively evaluates all eight possible three-bit input combinations and verifies:

1. Surface identity uniqueness.
2. Expanded set identity uniqueness.
3. Equivalence between pairwise surface activation and majority activation.
4. Deterministic static evaluation.

## 9. Design Principle

The central distinction is between activation and identity.

Majority activation determines whether a correlated surface is active. The complete Boolean signature determines which logical instance that surface represents.

Therefore:

\[
\boxed{
\text{Correlation}
\neq
\text{Identity}
\neq
\text{Activation}
}
\]

The architecture separates these three properties while retaining their logical relationship.

## 10. Scope and Limitations

This implementation is a finite Boolean model, not a temporal memetic system or an adaptive learning algorithm.

The eight unique identities arise from the eight possible three-bit input signatures. The expanded six-member representation does not create additional independent information because its last three members are derived from the original inputs.

The architecture can be extended to larger Boolean surfaces, additional correlation channels, and higher-order set constructors while preserving the same static-logic principles.

---

**Project:** Static Symmetric-Memetic Horizon Majority Function  
**Abbreviation:** SSMHMF  
**Language:** Python 3  
**Logic:** Deterministic combinational Boolean logic  
**Execution:** Single-pass exhaustive truth-table evaluation
