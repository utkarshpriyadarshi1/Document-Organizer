package com.updevlogics.repository;

import com.updevlogics.model.BackupRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BackupRepository extends JpaRepository<BackupRecord, Long> {
}
