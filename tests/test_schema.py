from tests.test_app.test_app.schema import schema


def test_schema():
    assert (
        str(schema)
        == """
schema {
  query: Query
  mutation: Mutation
}

type AuthorType implements SpriklNode {
  firstName: String!
  lastName: String!
  email: String!
  id: ID!
}

type BookType implements SpriklNode {
  title: String!
  id: ID!
  publisher: PublisherType
  allAuthors: [AuthorType!]
}

type BookTypeConnection {
  pageInfo: PageInfo!
  edges: [BookTypeEdge]!
  totalCount: Int!
}

type BookTypeEdge {
  node: BookType
  cursor: String!
}

input CreateRelayBookInput {
  title: String!
  clientMutationId: String
}

type CreateRelayBookPayload {
  title: String
  errors: [ErrorType]
  clientMutationId: String
}

type ErrorType {
  field: String
  messages: [String!]!
  path: [String!]
}

type Mutation {
  createRelayBook(input: CreateRelayBookInput!): CreateRelayBookPayload
  createRelayBookAdmin(input: CreateRelayBookInput!): CreateRelayBookPayload
  createRelayBookThrottle(input: CreateRelayBookInput!): CreateRelayBookPayload
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type PublisherType implements SpriklNode {
  name: String!
  address: String!
  id: ID!
  allBooks: [BookType!]
}

type Query {
  book(id: ID!): BookType
  books(before: String, after: String, first: Int, last: Int): BookTypeConnection
  bookAsAdmin(id: ID!): BookType
  booksAsAdmin(before: String, after: String, first: Int, last: Int): BookTypeConnection
  bookThrottled(id: ID!): BookType
  booksThrottled(before: String, after: String, first: Int, last: Int): BookTypeConnection
  booksFiltered(before: String, after: String, first: Int, last: Int, search: String): BookTypeConnection
  booksFilteredAsAdmin(before: String, after: String, first: Int, last: Int, search: String): BookTypeConnection
  booksFilteredThrottled(before: String, after: String, first: Int, last: Int, search: String): BookTypeConnection
}

interface SpriklNode {
  id: ID!
}
""".lstrip()
    )
