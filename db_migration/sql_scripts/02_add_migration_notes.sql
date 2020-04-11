\set ON_ERROR_STOP true
SET search_path to di_sueb_latein;

-- These calls adds a migration_note attribute to each table.
-- This attribute can be used to explain necessary changes to table entries to allow the foreign key constraint creation.

ALTER TABLE author
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE author_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE country
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE ddc_german
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE language
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE loc_assign
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE location
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE location_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE orig_assign
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE original
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE original_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE translation
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE translation_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE translator
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE translator_new
ADD COLUMN IF NOT EXISTS migration_notes VARCHAR(1023),
ADD COLUMN IF NOT EXISTS migration_generated BOOLEAN NOT NULL DEFAULT FALSE;
