/**
 * 認證工具函數
 * 提供註冊、登入、登出、獲取用戶資訊等核心認證功能
 * 支援郵箱註冊和用戶名註冊兩種方式
 */

import { supabase } from '../../../src/supabase/client';

/**
 * 生成虛擬郵箱（用於用戶名註冊）
 * @param {string} username - 用戶名
 * @returns {string} 虛擬郵箱地址
 */
function generateVirtualEmail(username) {
  return `${username.toLowerCase().replace(/[^a-z0-9]/g, '_')}@auth.local`;
}

/**
 * 用戶註冊
 * @param {string} identifier - 郵箱或用戶名
 * @param {string} password - 用戶密碼
 * @param {Object} options - 選項 { isUsername: boolean, metadata: Object }
 * @returns {Promise<{user: Object|null, error: Object|null}>}
 */
export async function registerUser(identifier, password, options = {}) {
  const { isUsername = false, metadata = {} } = options;

  let email = identifier;
  let username = metadata.username || identifier;

  // 如果是用戶名註冊，生成虛擬郵箱
  if (isUsername) {
    email = generateVirtualEmail(identifier);
  }

  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: {
        username,
        ...metadata,
      },
    },
  });

  return { user: data?.user, error };
}

/**
 * 用戶登入
 * @param {string} identifier - 郵箱或用戶名
 * @param {string} password - 用戶密碼
 * @returns {Promise<{session: Object|null, error: Object|null}>}
 */
export async function loginUser(identifier, password) {
  // 判斷是否是用戶名（不包含 @ 符號）
  const isUsername = !identifier.includes('@');

  let email = identifier;
  if (isUsername) {
    email = generateVirtualEmail(identifier);
  }

  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });

  return { session: data?.session, error };
}

/**
 * 用戶登出
 * @returns {Promise<{error: Object|null}>}
 */
export async function logoutUser() {
  const { error } = await supabase.auth.signOut();
  return { error };
}

/**
 * 獲取當前用戶資訊
 * @returns {Promise<{user: Object|null, profile: Object|null, error: Object|null}>}
 */
export async function getCurrentUser() {
  const { data: { user }, error: authError } = await supabase.auth.getUser();

  if (authError || !user) {
    return { user: null, profile: null, error: authError };
  }

  const { data: profile, error: profileError } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', user.id)
    .maybeSingle();

  return { user, profile, error: profileError };
}

/**
 * 更新用戶資料
 * @param {string} userId - 用戶 ID
 * @param {Object} updates - 更新欄位
 * @returns {Promise<{profile: Object|null, error: Object|null}>}
 */
export async function updateUserProfile(userId, updates) {
  const { data, error } = await supabase
    .from('profiles')
    .update({ ...updates, updated_at: new Date().toISOString() })
    .eq('id', userId)
    .select()
    .maybeSingle();

  return { profile: data, error };
}

/**
 * 重設密碼
 * @param {string} email - 用戶郵箱
 * @returns {Promise<{error: Object|null}>}
 */
export async function resetPassword(email) {
  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${window.location.origin}/reset-password`,
  });

  return { error };
}

/**
 * 更新密碼
 * @param {string} newPassword - 新密碼
 * @returns {Promise<{error: Object|null}>}
 */
export async function updatePassword(newPassword) {
  const { error } = await supabase.auth.updateUser({
    password: newPassword,
  });

  return { error };
}
