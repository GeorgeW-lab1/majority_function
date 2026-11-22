# SSMHMF — Static Symmetric-Memetic Horizon Majority Function

**A deterministic Boolean keyword-search, correlation, and hierarchical set-identification engine.**

## 1. Overview

SSMHMF is a static Boolean search architecture designed to identify correlated keyword patterns, activate matching surfaces, and construct larger logical sets from the resulting matches.

Rather than treating keyword search as a simple independent lookup, the architecture represents each search input as a Boolean signal. Relationships between signals are evaluated through symmetric pairwise conjunctions and majority functions.

When sufficient correlation exists between surface inputs, a new logical instance is activated. That instance retains its original Boolean signature and receives a unique identity, allowing it to be distinguished from other matching sets.

The system can be understood as a Boolean alternative to conventional keyword association and hierarchical retrieval.

Its primary operations are:

1. Keyword representation.
2. Boolean correlation.
3. Symmetric majority activation.
4. Surface signature identification.
5. Larger set construction.
6. Hierarchical classification.
7. Deterministic result identification.

All operations are static and deterministic.

## 2. Conceptual Search Architecture

```text
              SEARCH QUERY
                   |
                   v
          BOOLEAN KEYWORD INPUTS
               A, B, C
                   |
                   v
          CORRELATION SURFACE
             AB, AC, BC
                   |
                   v
           MAJORITY FUNCTION
          Two-of-three activation
                   |
                   v
          SURFACE IDENTIFICATION
           Unique Boolean signature
                   |
                   v
          HIERARCHICAL SET EXPANSION
           A, B, C, AB, AC, BC
                   |
                   v
          LARGER SET IDENTIFICATION
                   |
                   v
           RESULT CLASSIFICATION
```

## 3. Keyword Representation

Each keyword or search feature is represented by a Boolean value:

\[
K_i\in\{0,1\}
\]

Where:

- `1` indicates that a keyword or feature is present.
- `0` indicates that a keyword or feature is absent.

For example, a query containing three search concepts might be represented as:

\[
Q=(A,B,C)
\]

The Boolean representation allows the search system to evaluate relationships between concepts without requiring sequential processing.

In a practical implementation, a separate deterministic keyword-matching stage would convert query text and indexed documents into Boolean feature vectors.

## 4. Symmetric Correlation Surface

The surface evaluates pairwise relationships:

\[
S(Q)=\{AB,AC,BC\}
\]

Where:

\[
AB=A\land B
\]

\[
AC=A\land C
\]

\[
BC=B\land C
\]

Each conjunction represents a pairwise keyword relationship.

For example:

- `AB` identifies the simultaneous presence of concepts A and B.
- `AC` identifies the simultaneous presence of concepts A and C.
- `BC` identifies the simultaneous presence of concepts B and C.

The surface is symmetric: no individual input has priority.

## 5. Majority-Based Search Activation

The majority function determines whether the search surface contains sufficient correlation.

\[
M(A,B,C)=(AB)\lor(AC)\lor(BC)
\]

When any two of the three inputs are active, the surface activates.

In search terminology, this represents a minimum correlation threshold for constructing a larger result set.

An activated surface does not automatically imply semantic relevance. It indicates that the specified Boolean matching conditions have been satisfied.

## 6. Unique Instance Identification

A critical property of the architecture is the separation of activation from identity.

A majority output alone cannot distinguish between different matching configurations.

Therefore, the complete Boolean signature is preserved:

\[
I_s=4A+2B+C
\]

This creates eight possible surface identities.

For example:

| Signature | Identity | Activated |
|---|---:|---:|
| 000 | 0 | No |
| 001 | 1 | No |
| 010 | 2 | No |
| 011 | 3 | Yes |
| 100 | 4 | No |
| 101 | 5 | Yes |
| 110 | 6 | Yes |
| 111 | 7 | Yes |

Each signature remains distinguishable even when multiple configurations produce the same majority result.

## 7. Hierarchical Keyword Set Construction

An activated surface can construct a larger logical set:

\[
\mathcal S(Q)=\{A,B,C,AB,AC,BC\}
\]

This represents both the original keyword features and their pairwise correlations.

In a keyword-search application, the expanded set can represent:

- Original matched terms.
- Pairwise keyword combinations.
- Correlated search features.
- Candidate document classifications.
- Higher-order retrieval relationships.

The larger set preserves the original signature, making its identity recoverable.

## 8. Larger Set Identification

The expanded set has a six-bit representation:

\[
I_{\mathcal S}=
32A+16B+8C+4AB+2AC+BC
\]

Because the original three-bit signature is retained, the expanded set has a unique identity for every possible original input configuration.

This provides deterministic identification without requiring a separate mutable registry.

## 9. Parent Majority Classification

The expanded set can be classified using a four-of-six majority threshold:

\[
P(\mathcal S)=
\begin{cases}
1 & \text{if } \sum\mathcal S\geq4\\
0 & \text{otherwise}
\end{cases}
\]

In a retrieval context, this represents a second-level Boolean classification over the expanded feature set.

Further levels can be constructed by introducing additional Boolean inputs and higher-order conjunctions.

## 10. Keyword Search Application

The architecture can be used as the logical foundation for a small Boolean retrieval engine.

A possible application pipeline is:

**Query encoding:** Convert a user query into Boolean keyword features.

**Document encoding:** Represent indexed documents using corresponding Boolean feature vectors.

**Surface correlation:** Calculate pairwise keyword intersections.

**Majority activation:** Determine whether the required correlation threshold is met.

**Instance identification:** Preserve the complete matching signature.

**Set construction:** Build larger feature sets from the original matches and their relationships.

**Result classification:** Apply higher-level Boolean thresholds to distinguish candidate result sets.

A production implementation would also need document identifiers, an inverted index, and a mapping from Boolean signatures to actual documents.

## 11. Static Logic Properties

| Property | Implementation |
|---|---|
| Search representation | Boolean |
| Keyword activation | Binary |
| Correlation | Pairwise AND |
| Surface activation | Two-of-three majority |
| Identity | Complete Boolean signature |
| Set expansion | Six-member representation |
| Classification | Four-of-six threshold |
| Feedback | None |
| Temporal memory | None |
| Adaptive learning | None |
| Determinism | Guaranteed |

## 12. Implementation

The Python implementation is contained in:

`smhmf.py`

Run:

```bash
python smhmf.py
```

The program evaluates all eight possible three-bit signatures and verifies:

- Unique surface identities.
- Unique expanded-set identities.
- Majority and surface equivalence.
- Deterministic Boolean evaluation.

## 13. Future Extensions

Potential extensions include:

- Larger keyword vectors.
- N-input majority functions.
- Higher-order Boolean correlation surfaces.
- Hierarchical document classification.
- Multi-level keyword set expansion.
- Static Boolean query matching.
- Distinct document identity encoding.
- Exact-match and partial-match retrieval modes.

These extensions can retain the static Boolean architecture without introducing temporal feedback.

## 14. Central Design Principle

The system distinguishes three separate logical properties:

\[
\boxed{
\text{Correlation}
\neq
\text{Activation}
\neq
\text{Identity}
}
\]

Correlation establishes relationships between keywords.

Activation determines whether a matching surface satisfies the majority condition.

Identity preserves which exact Boolean configuration produced the match.

This separation is fundamental to constructing uniquely identifiable search sets from symmetric Boolean surfaces.

---

**Project:** Static Symmetric-Memetic Horizon Majority Function  
**Abbreviation:** SSMHMF  
**Application:** Boolean keyword search and hierarchical retrieval  
**Language:** Python 3  
**Architecture:** Static combinational logic  
**Execution:** Deterministic, single-pass evaluation
